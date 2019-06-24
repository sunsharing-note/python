#!/usr/bin/env python
#--coding:utf-8--
import requests
# import ast
# import config
import sys,json,re
import test


class Harbor_API:
    def __init__(self):
        self.login_user = 'admin'
        self.login_password = 'Harbor12345'
        ## Harbor相关登录配置
        self.login_url = 'https://xxxxx/login'
        self.projects_url = 'https://xxxxx/api/projects'
        self.repo_url = "https://xxxxx/api/repositories?project_id="
        self.image_url = "https://xxxxx/api/repositories/"
        # "https://xxxxx/api/repositories/testrepo%2Fcentos/tags/
        self.headers = {
            'Host':'xxxxx',
            'Origin':'https://xxxxx',
            'Referer':'https://xxxxx/harbor/sign-in',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        self.data = { 'principal': self.login_user, 'password': self.login_password }
        self.s = requests.Session()
    def get_repo(self,project_id):
        # 用join
        url = self.repo_url + str(project_id)
        # print(url)
        res = self.s.get(url)
        
        all_repo = json.loads(res.text)
        repo_data = []
        for repo in all_repo:
            data = {}
            data["id"] = repo["id"]
            data["name"] = repo["name"]
            repo_data.append(data)
        return repo_data
    def get_image(self,project_id,repo_name):
        # 用join
        url = self.repo_url+str(project_id)+("&q=%s") % repo_name
        # print(url)
        res = self.s.get(url)
        count = json.loads(res.text)[0]["tags_count"]
        return count
    def get_image_tags(self,project_name,repo_name):
        # 用join
        url = self.image_url+project_name+"%2F"+repo_name+"/tags/"
        # print(url)
        res = self.s.get(url)
        all_tags = json.loads(res.text)
        tags_data = []
        for tag in all_tags:
            tags_data.append(tag["name"])
        #print("tags_data",tags_data)
        # 获取类型
        tags_seri1 = []
        for i in tags_data:
            tags_seri1.append(i[0:6])
        # 类型去重
        tags_seri2 = []
        [tags_seri2.append(i) for i in tags_seri1 if not i in tags_seri2]
        # 根绝类型统计个数
        tags_seri3 = []
        for i in tags_seri2:
            data = {}
            data["name"] = i
            data["count"] = tags_seri1.count(i)
            tags_seri3.append(data)
        return tags_seri3
    def get_projects(self):
        #res = self.s.get(self.projects_url)
        # res = self.s.get(self.projects_url)
        res = self.s.get(self.projects_url)
        # repo_project = ast.literal_eval(res.text.encode("utf-8"))
        repo_project = json.loads(res.text)
        project_data = []
        for project in repo_project:
            data = {}
            # project_data[str(project['project_id']] = project['project_id']
            data["id"] = project["project_id"]
            data["name"] = project["name"]
            project_data.append(data)
        return project_data
    def delete_image(self,all_tags,project_name,repo_name,seri):
        url = self.image_url+project_name+"%2F"+repo_name+"/tags/"
        # print(url)
        res = self.s.get(url)
        all_tags = json.loads(res.text)
        tags_data = []
        for tag in all_tags:
            tags_data.append(tag["name"])
        #print("tags_data",tags_data)
        # 用join
        url2 = self.image_url + project_name + "%2F" + repo_name + "/tags/"
        # all_tags = self.get_image_tags(project_name,repo_name)
        tag = []
        
        for i in tags_data:
            ret = re.findall(r"%s.*" % seri,i)
            #print(ret)
            if not ret:
                continue
            else:
                tag.append(ret[0])
        #print(tag)
        for i in tag:
            url2 = url + i
            print(url2)
            ret = self.s.delete(url2)
        return ret

    def login(self):
        ## 创建Session登录
        res = self.s.post(self.login_url, headers=self.headers, data=self.data,verify=False)
        return res.status_code

## 入口
if __name__ == '__main__':
    ss = Harbor_API()
    status_code = ss.login()
    #print(status_code)
    if status_code == 200:
        all_projects = ss.get_projects()
        # print(all_projects)
        print("--------当前harbor下以下项目-------")
        id_list = []
        for i in all_projects: 
            
            print("id:%s-----项目名:%s" % (i["id"],i["name"]))
            id_list.append(i["id"])
        while True:
            project_id = input("请输入上面的项目id，查看该项目下的镜像仓库：")
            project_id = int(project_id.strip())
            flag = project_id in id_list
            if flag:
                all_repo = ss.get_repo(project_id)
                print("--------当前项目下有以下镜像仓库-------")
                repo_id_list = []
                for i in all_repo:
                    print("id:%s-----仓库名:%s" % (i["id"],i["name"]))
                    repo_id_list.append(i["id"])
                # print(repo_id_list)
                while True:
                    repo_id = input("请输入上面的仓库id，查看该项目下的镜像类别和数量：")
                    repo_id = repo_id.strip()
                    # print(repo_id)
                    # print(repo_id_list)
                    # print(all_repo)
                    # flag = repo_id in repo_id_list
                   
                    if int(repo_id) in repo_id_list:
                        for i in all_repo:
                            if i["id"] == int(repo_id):
                                repo_name = i["name"]
                                count = ss.get_image(project_id,repo_name)
                                repo_name = test.tt(repo_name)
                        # print(repo_name)
                        # print(count)
                        for i in all_projects:
                            if i["id"] == project_id:
                                project_name = i["name"]
                                
                        # print(project_name)        
                        all_tags = ss.get_image_tags(project_name,repo_name)
                        #print(all_tags)
                        for i in all_tags:
                            print("项目为%s,仓库为%s的镜像类型有%s，数量为%s" %(project_name,repo_name,i["name"],i["count"]))
                        seri_name = []
                        for i in all_tags:
                            seri_name.append(i["name"])
                        while True:
                            seri = input("请输入要删除的镜像类型,如201805：").strip()
                            if seri == "r" or seri == "b":
                                print("返回到上一级")
                            flag = seri in seri_name
                            if flag:
                                for i in all_tags:
                                    if i["name"] == seri:
                                        print("类型为%s，其数量为%s个" %(seri,i["count"]))
                                        print("project %s  repo %s seri %s" %(project_name,repo_name,seri))
                                        #print(all_tags)
                                        ret = ss.delete_image(all_tags,project_name,repo_name,seri)
                                        if ret:
                                            print("删除成功")
                                            quit()
                            else:
                                print("false")

                            
                    else:
                        print("该仓库id不存在，请重新输入。")  
            else:
                print("该id不存在，请重新输入。")
            
  
