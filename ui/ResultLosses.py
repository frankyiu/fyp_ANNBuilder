from ui.ResultMetric import ResultMetric

class ResultLosses(ResultMetric):
    def __init__(self, metric_type, parent=None):
        super().__init__(metric_type, parent)
        self.f_string = metric_type + ": {:.3f}"
        self.showMetric()
