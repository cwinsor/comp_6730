python train.py --dataset=cora --dropout=0.5 --weight_decay=5e-3 --epochs=500
python train.py --dataset=enzymes --weight_decay=5e-3 --num_layers=3 --epochs=500

python train.py --dataset=cora    --model_type='GraphSage' --dropout=0.5 --weight_decay=5e-3 --epochs=500
python train.py --dataset=enzymes --model_type='GAT' --weight_decay=5e-3 --num_layers=3 --epochs=500

