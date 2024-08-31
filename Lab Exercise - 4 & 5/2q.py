from abc import ABC, abstractmethod

class DataAnalyzer(ABC):
    def analyze(self, data):
        pass

class TextDataAnalyzer(DataAnalyzer):
    def analyze(self, data):
        try:
            if not isinstance(data, str):
                raise TypeError("Data is not of type str")
            word_count = len(data.split())
            return f"Text analysis: {word_count} words."
        except TypeError as te:
            return f"TextDataAnalyzer TypeError: {te}"
        except Exception as e:
            return f"TextDataAnalyzer Unexpected Error: {e}"

class NumericDataAnalyzer(DataAnalyzer):
    def analyze(self, data):
        try:
            if not isinstance(data, list):
                raise TypeError("Data is not a list")
            if not all(isinstance(i, (int, float)) for i in data):
                raise ValueError("Data contains non-numeric values")
            average = sum(data) / len(data)
            return f"Numeric analysis: Average = {average}"
        except TypeError as te:
            return f"NumericDataAnalyzer TypeError: {te}"
        except ValueError as ve:
            return f"NumericDataAnalyzer ValueError: {ve}"
        except Exception as e:
            return f"NumericDataAnalyzer Unexpected Error: {e}"


class AnalysisError(Exception):
    pass

if __name__ == "__main__":
    analyzers = [TextDataAnalyzer(), NumericDataAnalyzer()]

    data_entries = ["This is a sample text for analysis.", [10, 20, 30, 40], "Invalid Numeric Data", [10, "20", 30]]

    for analyzer in analyzers:
        for data in data_entries:
            result = analyzer.analyze(data)
            print(result)
