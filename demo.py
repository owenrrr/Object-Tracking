from mosse import mosse
import argparse
import os

parse = argparse.ArgumentParser()
parse.add_argument('--lr', type=float, default=0.125, help='the learning rate')
parse.add_argument('--sigma', type=float, default=100, help='the sigma')
parse.add_argument('--num_pretrain', type=int, default=128, help='the number of pretrain')
parse.add_argument('--rotate', action='store_true', help='if rotate image during pre-training.')
parse.add_argument('--record', action='store_true', help='record the frames')


def _get_list_dirs(dir_path):
    dirs = []
    for frame in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, frame)):
            dirs.append(frame)
    return dirs


if __name__ == '__main__':
    args = parse.parse_args()
    dir_path = 'datasets/'
    dirs = _get_list_dirs(dir_path)
    for sub_dir in dirs:
        tracker = mosse(args, dir_path, sub_dir, False)
        tracker.start_tracking()


    # 需要手动：uwhgtyrn,
    # TODO 手动生成ground-truth.txt
    # tracker = mosse(args, dir_path, 'uwhgtyrn', True)
    # tracker.start_tracking()

