import torch.nn as nn
import torch
from roi_pooling.modules.roi_pool import RoIPool

class RoINet(nn.Module):
    def __init__(self):
        # TODO: Finished this part.
        super(RoINet, self).__init__()
        self.roi_pool = RoIPool(4,7,1.0/16)

    def forward(self,feature,rois):        
        pooled_features = self.roi_pool(feature,rois)
        return pooled_features

if __name__ == '__main__':

    databuffer = torch.zeros([2, 16 * 4, 64, 64])
    print('buffer size:',databuffer.size())
    # param rois: (1, N, 4) N refers to bbox num, 4 represent (ltx, lty, w, h)
    rois = torch.autograd.Variable(torch.FloatTensor([[0,1,2,7,8],[0,3,3,8,8]]),requires_grad=False)
    roinet = RefineNet()
    print('roi_data_shape:',rois.size())
    out = roinet(databuffer, rois)
    print('roi done.')
    print('roi feature size:',out.size())