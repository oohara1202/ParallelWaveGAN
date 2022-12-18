import os
import shutil
from pathlib import Path

db_root = '/work/abelab4/s_koha/work/dataset/STUDIES_22k_reconst/Teacher'
base_dir = 'data'

train_types = ['train_nodev', 'dev', 'eval']
dir_types = ['tr_no_dev', 'dev', 'eval1']

# ディレクトリの初期化
try:
    shutil.rmtree(base_dir)
except FileNotFoundError:
    pass
os.mkdir(base_dir)

for train_type, dir_type in zip(train_types, dir_types):
    os.mkdir(os.path.join(base_dir, train_type))
    p = Path(os.path.join(db_root, dir_type))
    wav_files = list(p.glob('*.wav'))
    wav_files.sort()
    
    scp_path = os.path.join(base_dir, train_type, 'wav.scp')
    with open(scp_path, mode='w') as f:
        for wav_file in wav_files:
            basename = os.path.splitext(os.path.basename(wav_file))[0]
            basename = basename.split('-', 1)
            basename = '_'.join(basename)
            s = 'teacher{} {}\n'.format(basename, wav_file)
            f.write(s)

    # segmentsのコピー
    espnet_dir = '/work/abelab4/s_koha/shinycolors_tts/egs2/abelab/03_studies/data/'
    shutil.copyfile(
        os.path.join(espnet_dir, dir_type, 'segments'),
        os.path.join(base_dir, train_type, 'segments')
    )
