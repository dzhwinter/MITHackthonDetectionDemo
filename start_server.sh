#!/bin/bash
wget https://s3.us-east-2.amazonaws.com/models.paddlepaddle/02.recognize_digits/param.tar
wget https://s3.us-east-2.amazonaws.com/models.paddlepaddle/02.recognize_digits/inference_topology.pkl
nvidia-docker run --name recog_digits_serv -d -v $PWD:/data -p 8100:80 -e WITH_GPU=1 paddlepaddle/book:serve-gpu
