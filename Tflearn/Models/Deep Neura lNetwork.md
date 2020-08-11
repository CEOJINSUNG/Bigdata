# Deep Nerual Network Model

### [기본적인 형태]

#### tflearn.models.dnn.DNN
    (
    network, : Tensor이 기본적으로 쓰인다
    clip_gradients=5.0,
    tensorboard_verbose = 0, [int] : verbose는 학습 중 출력되는 문구(log)를 설정 딥러닝의 진행상황을 알려줌
    tensorboard_dir='/tmp/tflearn_logs/', [str] : tensorboard log가 저장되는 공간을 말함
    checkpoint_path=None,[str] : Model의 Check point 저장경로를 말함
    best_checkpoint_path=None, [str] : 훈련 중 가장 높은 유효값을 저장 하는 경로
    max_checkpoints=None, [int] : 가장 큰 Check point 값
    session = None, [Session] : A session for running ops 유저의 코드가 실행되는 하나의 작업 단위
    best_val_accuracy = 0.0 [float] : 가장 최소한의 정확성을 설정해 모델의 가중치를 미리 설정해 놓아 빠르게 저장하고 다시 돌릴 수 있다.
    )

##### 속성(Atrributes)
    - trainer [Trainer] : 모델 Training을 다룸
    - predictor [Predictor] : 모델 Prediction을 다룸
    - session [Session] : 현재 모델 Session을 다룸

#### Methods

##### evaluate(X,Y,batch_size=128) : 모델을 평가할 때 사용하는 함수인 듯 하다.
    evaluate(
    X, : list나 dict 배열이 들어감, Data to feed to train model.
    Y, : list나 dict 배열이 들어감, Targets to feed to train model.
    batch_size=128 : 한번의 batch마다 주는 데이터 샘플의 size를 말함
    )
    
    Return metric(s) score
    
##### fit
    (
    X_inputs,
    Y_targets,
    n_epoch=10, : epoch의 횟수를 말하는데 이는 역전파 알고리즘이 한번 왔다갔다 하면 한번의 epoch
    validation_set=None,
    show_metric=False, 
    batch_size=None,
    shuffle=none,
    snapshot_epoch=True,
    snapshot_step=None,
    excl_trainops=None,
    validation-batch_size=None,
    run_id=None,
    callbacks=[]
    )
