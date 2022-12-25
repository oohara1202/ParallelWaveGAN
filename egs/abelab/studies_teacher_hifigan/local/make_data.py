import os
import shutil

espnet_dir = '/work/abelab4/s_koha/shinycolors_tts/egs2/abelab_hara/02_studies/data'
data_dir = 'data'

train_types = ['train_nodev', 'dev', 'eval']
dir_types = ['tr_no_dev', 'dev', 'eval1']

# ディレクトリの初期化
try:
    shutil.rmtree(data_dir)
except FileNotFoundError:
    pass
os.mkdir(data_dir)

for train_type, dir_type in zip(train_types, dir_types):
    os.mkdir(os.path.join(data_dir, train_type))

    # wav.scpのコピー
    shutil.copyfile(
        os.path.join(espnet_dir, dir_type, 'wav.scp'),
        os.path.join(data_dir, train_type, 'wav.scp')
    )
    # segmentsのコピー
    shutil.copyfile(
        os.path.join(espnet_dir, dir_type, 'segments'),
        os.path.join(data_dir, train_type, 'segments')
    )
