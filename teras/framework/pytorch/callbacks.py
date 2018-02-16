import torch

from teras.training.callbacks import Saver as _Saver
import teras.logging as Log


class Saver(_Saver):

    def __init__(self, model, basename, directory='', context=None,
                 interval=1, save_from=None, name="pytorch.saver", **kwargs):
        super(Saver, self).__init__(model, basename, directory, context,
                                    interval, save_from, name, **kwargs)

    def on_epoch_end(self, data):
        epoch = data['epoch']
        if self._save_from is not None and data['epoch'] < self._save_from:
            return
        if epoch % self._interval == 0:
            model_file = "{}.{}.mdl".format(self._basename, epoch)
            Log.i("saving the model to {} ...".format(model_file))
            torch.save(self._model.state_dict(), model_file)
