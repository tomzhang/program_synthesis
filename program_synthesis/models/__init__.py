from .karel_model import KarelLGRLModel, KarelLGRLRefineModel
from .karel_trace_model import TracePredictionModel


def get_model(args):
    MODEL_TYPES = {
        'karel-lgrl': KarelLGRLModel,
        'karel-lgrl-ref': KarelLGRLRefineModel,
        'karel-trace-pred': TracePredictionModel,
    }
    return MODEL_TYPES[args.model_type](args)
