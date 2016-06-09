#!/bin/sh

rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm  &&  yum install docker-io --enablerepo=epel  &&  service docker start

#Solved: Cannot retrieve metalink for repository: epel. Please verify its path and try again
#edit /etc/yum.repos.d/epel.repo , replace https with http and Save it.

