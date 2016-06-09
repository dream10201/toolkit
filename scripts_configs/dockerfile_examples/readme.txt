
一步步演示了如何自己编写c++的tcp服务并打包成docker镜像,然后部署,运行及测试该tcp服务是否正常.

本文档假设你已经安装并启动好了docker服务, 否则请按照tools/中的docker_install_centos6.5_tested.sh进行一键安装运行docker服务.


1) 一键部署自己的应用:

cd docker_operation/ && ./1_docker.build.sh && ./2_docker.run.sh && cd ../ 


2) 测试部署应用是否正常:

cd source/ && python test_client.py && cd ../


3) 导出及分发:
cd docker_operation/ && ./3_export.sh <container id> && cd ../

注意,默认导出的tar包较大,使用bzip2 -9 可以高效压缩.分发时把压缩包拷给不同的人即可


4) 导入及运行:
cd docker_operation/ && ./4_import.sh && ./5_docker.run.sh && cd ../

注意, 如果在同一机器上测试应该删除原有容器和镜像. 删除容器可以使用tools中的脚本docker_rm_all_containers.sh, 删除镜像使用docker rmi <image id>



