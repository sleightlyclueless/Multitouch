import math
from TuioGestures import TuioGestures, Point2D, GestureTemplate

class GeometricRecognizer:
    def __init__(self):
        self.TuioGestures = TuioGestures()

        self.HalfDiagonal = 0
        self.AngleRange = 0
        self.AnglePrecision = 0
        self.GoldenRatio = 0
        self.NumPointsInGesture = 0
        self.SquareSize = 0
        self._shouldIgnoreRotation = False
        self.Templates = []

        self.RotationInvariance = False
        self.AngleRange = 45.0 if self._shouldIgnoreRotation else 15.0

        self.NumPointsInGesture = 128
        self.SquareSize = 250
        self.HalfDiagonal = 0.5 * math.sqrt((250.0 * 250.0) + (250.0 * 250.0))
        self.RotationInvariance = False
        self.AnglePrecision = 2.0
        self.GoldenRatio = 0.5 * (-1.0 + math.sqrt(5.0))
        self.load_templates()

    @property
    def RotationInvariance(self):
        return self._shouldIgnoreRotation

    @RotationInvariance.setter
    def RotationInvariance(self, value):
        self._shouldIgnoreRotation = value
        self.AngleRange = 45.0 if self._shouldIgnoreRotation else 15.0

    def load_templates(self):
        for template in TuioGestures.templates:
            self.Templates.append(GestureTemplate (template.Name, self.NormalizePath(template.Path)))

    
    def recognize(self, points:list):
        if not self.Templates:
            print("No templates loaded, so no symbols to match.")
            return RecognitionResult("Unknown", 1)

        points = self.NormalizePath(points)
        best_distance = float("inf")
        best_template = None

        for template in self.Templates:
            distance = self.DistanceAtBestAngle(points, template)
            if distance < best_distance:
                best_distance = distance
                best_template = template

        score = 1.0 - (best_distance / self.HalfDiagonal)

        if best_template is None:
            return RecognitionResult("Unknown", 1)

        best_match = RecognitionResult(best_template.Name, score)
        return best_match


#===============================================================================
#UTIL

    def NormalizePath(self, points:list):
        points = self.Resample(points)

        if self.RotationInvariance:
            points = self.RotateToZero(points)

        points = self.ScaleToSquare(points)
        points = self.TranslateToOrigin(points)
        return points

    def TranslateToOrigin(self, points):
        c = self.Centroid(points)
        newPoints = []
        for point in points:
            qx = point.x - c.x
            qy = point.y - c.y
            newPoints.append(Point2D(qx, qy))
        return newPoints

    def ScaleToSquare(self, points):
        box = self.BoundingBox(points)
        newPoints = []
        for point in points:
            scaledX = point.x * (self.SquareSize / box.Width)
            scaledY = point.y * (self.SquareSize / box.Height)
            newPoints.append(Point2D(scaledX, scaledY))
        return newPoints

    def BoundingBox(self, points):
        minX = float('inf')
        maxX = float('-inf')
        minY = float('inf')
        maxY = float('-inf')

        for point in points:
            if point.x < minX:
                minX = point.x
            if point.x > maxX:
                maxX = point.x
            if point.y < minY:
                minY = point.y
            if point.y > maxY:
                maxY = point.y

        return Rectangle(minX, minY, maxX - minX, maxY - minY)

    def RotateToZero(self, points):
        c = self.Centroid(points)
        rotation = math.atan2(c.y - points[0].y, c.x - points[0].x)
        points = self.RotateBy(points, -rotation)
        return points

    def RotateBy(self, points, rotation):
        centroid = self.Centroid(points)
        cos = math.cos(rotation)
        sin = math.sin(rotation)
        newPoints = []

        for point in points:
            qx = (point.x - centroid.x) * cos - (point.y - centroid.y) * sin + centroid.x
            qy = (point.x - centroid.x) * sin + (point.y - centroid.y) * cos + centroid.y
            newPoints.append(Point2D(qx, qy))

        return newPoints

    def Centroid(self, points):
        x = 0.0
        y = 0.0

        for point in points:
            x += point.x
            y += point.y

        x /= len(points)
        y /= len(points)
        return Point2D(x, y)

    def Resample(self, points:list):
        interval = self.PathLength(points) / (self.NumPointsInGesture - 1)
        d = 0.0
        newPoints = [points[0]]

        i = 1
        while i < len(points):
            currentPoint = points[i]
            previousPoint = points[i - 1]
            distance = self.GetDistance(previousPoint, currentPoint)

            if (d + distance) >= interval:
                qx = previousPoint.x + ((interval - d) / distance) * (currentPoint.x - previousPoint.x)
                qy = previousPoint.y + ((interval - d) / distance) * (currentPoint.y - previousPoint.y)
                point = Point2D(qx, qy)
                newPoints.append(point)
                points.insert(i, point)
                d = 0.0
            else:
                d += distance

            i += 1
        
        if len(newPoints) == (self.NumPointsInGesture - 1):
            newPoints.append(points[-1])

        return newPoints

    def PathLength(self, points:list):
        distance = 0.0
        for i in range(1, len(points)):
            distance += self.GetDistance(points[i - 1], points[i])
        return distance

    def GetDistance(self, p1:Point2D, p2:Point2D):
        #print("ILTAM SUMRA", p1, p2)
        dX = p2.x - p1.x
        dY = p2.y - p1.y
        distance = math.sqrt((dX * dX) + (dY * dY))
        return distance

    def DistanceAtBestAngle(self, points, template):
        startRange = -self.AngleRange
        endRange = self.AngleRange
        x1 = self.GoldenRatio * startRange + (1.0 - self.GoldenRatio) * endRange
        f1 = self.DistanceAtAngle(points, template, x1)
        x2 = (1.0 - self.GoldenRatio) * startRange + self.GoldenRatio * endRange
        f2 = self.DistanceAtAngle(points, template, x2)

        while abs(endRange - startRange) > self.AnglePrecision:
            if f1 < f2:
                endRange = x2
                x2 = x1
                f2 = f1
                x1 = self.GoldenRatio * startRange + (1.0 - self.GoldenRatio) * endRange
                f1 = self.DistanceAtAngle(points, template, x1)
            else:
                startRange = x1
                x1 = x2
                f1 = f2
                x2 = (1.0 - self.GoldenRatio) * startRange + self.GoldenRatio * endRange
                f2 = self.DistanceAtAngle(points, template, x2)

        return min(f1, f2)

    def DistanceAtAngle(self, points, template, rotation):
        newPoints = self.RotateBy(points, rotation)
        return self.PathDistance(newPoints, template.Path)

    def PathDistance(self, pts1, pts2):
        if len(pts1) != len(pts2):
            return float('inf')

        distance = sum([self.GetDistance(pts1[i], pts2[i]) for i in range(len(pts1))])
        return distance / len(pts1)


class Rectangle:
    def __init__(self, x:float, y:float, width:float, height:float):
        self.x = x
        self.y = y
        self.Width = width
        self.Height = height

class RecognitionResult:
    def __init__(self, name, score):
        self.Name = name
        self.Score = score
