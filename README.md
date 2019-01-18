Forked From https://github.com/longcw/faster_rcnn_pytorch  
**Delete almost everything form original repo except roi pooling.**
Now this is a pure roi-pooling repo.

# Get Start
First clone this repo on local computer.
`git clone https://github.com/longcw/faster_rcnn_pytorch`

# Make 
Execute 'make.sh'.

# Demo
Example code is included in `demo.py`.

# Other
BugFixed: 
- Comment following lines to enable batch_size > 1 :  
https://github.com/longcw/faster_rcnn_pytorch/blob/0a398a2d48f94dda19f96db1fad0f5139f533002/faster_rcnn/roi_pooling/src/roi_pooling_cuda.c#L27-L30  
https://github.com/longcw/faster_rcnn_pytorch/blob/0a398a2d48f94dda19f96db1fad0f5139f533002/faster_rcnn/roi_pooling/src/roi_pooling_cuda.c#L69-L72  
- Fix a subtle bug in the cuda backwards code for roi pooling that manifests itself only when batch size is > 1. Mentioned at https://github.com/longcw/faster_rcnn_pytorch/issues/52#issuecomment-351163368    

