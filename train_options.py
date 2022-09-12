import argparse

#training options
parser = argparse.ArgumentParser(description='Train Change Detection Models')

# training parameters
parser.add_argument('--num_epochs', default=10, type=int, help='train epoch number')
parser.add_argument('--batchsize', default=4, type=int, help='batchsize')
parser.add_argument('--val_batchsize', default=1, type=int, help='batchsize for validation')
parser.add_argument('--num_workers', default=12, type=int, help='num_workers')
parser.add_argument('--n_class', default=2, type=int, help='number of class')
parser.add_argument('--gpu_id', default="0", type=str, help='which gpu to run.')
parser.add_argument('--lr', type=float, default=0.0005, help='initial learning rate for adam')
parser.add_argument('--beta1', type=float, default=0.9, help='momentum term of adam')
parser.add_argument('--suffix', default=['.png','.jpg','.tif'], type=list, help='the suffix of the image files.')
parser.add_argument('--wDice', type=float, default=0.1, help='weight of dice loss')


# path for loading data
parser.add_argument('--train1_dir', default='E:/BaiduNetdiskDownload/SYSU-CD/train1/time1', type=str, help='t1 image path for training')
parser.add_argument('--train2_dir', default='E:/BaiduNetdiskDownload/SYSU-CD/train1/time2', type=str, help='t2 image path for training')
parser.add_argument('--label_train', default='E:/BaiduNetdiskDownload/SYSU-CD/train1/label', type=str, help='label path for training')

parser.add_argument('--val1_dir', default='E:/BaiduNetdiskDownload/SYSU-CD/val1/time1', type=str, help='t1 image path for validation')
parser.add_argument('--val2_dir', default='E:/BaiduNetdiskDownload/SYSU-CD/val1/time2', type=str, help='t2 image path for validation')
parser.add_argument('--label_val', default='E:/BaiduNetdiskDownload/SYSU-CD/val1/label', type=str, help='label path for validation')


# network saving and loading parameters
parser.add_argument('--model_dir', default='./epochs/CDD/', type=str, help='save path for CD model')
parser.add_argument('--sta_dir', default='./statistics/CDD.csv', type=str, help='statistics')








