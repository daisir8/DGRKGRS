# DGRKGRS
基于多模态知识图谱的智能旅游推荐系统
2023.4.15 新增数据库文件，可以直接demo该系统。


总体思路：
我的项目不太方便demo。忘记记录需要的第三方库了。本来数据库也没有，更难demo，我已经给加上了。
得在电脑下载django框架，然后运行该项目，根据报错信息下载对应的第三方库。
最后呈现的系统是有一个前台展示一些静态的旅游资源，然后登陆后有个问答界面和多模态知识图谱界面，有个机器人和你聊天对话，会根据你对景点的评分或是你所说的喜欢的景点为你推荐一些景点。
（思路是如此的，但是我的推荐效果可能不一定准确，最理想的状态是后台users-items映射关系数据，也就是用户对景点的评分以及景点图谱数据都输入到MKR模型中，通过多特征学习增强知识图谱在推荐系统中作用的这一模型，得到其余用户对景点的评分数据，然后根据评分从高到低排序，呈现给用户 模型训练出来的 认为用户最有可能评分高的景点，然后完成整个推荐系统。而具体MKR模型的输入以及输出，不在该系统中体现，该系统只是展示结果。）
![image](https://user-images.githubusercontent.com/67043197/232212365-8626d6cf-087c-46e3-97f8-d4060b31b011.png)
![image](https://user-images.githubusercontent.com/67043197/232212376-7deefa0d-8037-46d1-ae0b-e302bf43ae42.png)
![image](https://user-images.githubusercontent.com/67043197/232212391-1e6ee283-a037-430b-a1fe-f34c35af48b3.png)
![image](https://user-images.githubusercontent.com/67043197/232212400-c5e6fcf2-4e21-43c1-a73c-2b48d5631cef.png)
![image](https://user-images.githubusercontent.com/67043197/232212404-48e38686-5bd6-4128-a012-2baea863d32e.png)

