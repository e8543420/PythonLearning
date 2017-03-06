#coding=utf-8 
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name: pymssqlTest.py
# Purpose: ���� pymssql�⣬�ÿ⵽�������أ�http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
#
# Author: scott
#
# Created: 04/02/2012
#-------------------------------------------------------------------------------

import pymssql


class MSSQL:
    """
    ��pymssql�ļ򵥷�װ
    pymssql�⣬�ÿ⵽�������أ�http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    ʹ�øÿ�ʱ����Ҫ��Sql Server Configuration Manager���潫TCP/IPЭ�鿪��

    �÷���

    """

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        �õ�������Ϣ
        ����: conn.cursor()
        """
        if not self.db:
            raise(NameError,"û���������ݿ���Ϣ")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"�������ݿ�ʧ��")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        ִ�в�ѯ���
        ���ص���һ������tuple��list��list��Ԫ���Ǽ�¼�У�tuple��Ԫ����ÿ�м�¼���ֶ�

        ����ʾ����
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #��ѯ��Ϻ����ر�����
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        ִ�зǲ�ѯ���

        ����ʾ����
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def main():
## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
## #���ص���һ������tuple��list��list��Ԫ���Ǽ�¼�У�tuple��Ԫ����ÿ�м�¼���ֶ�
## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

    ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
    resList = ms.ExecQuery("SELECT id,weibocontent FROM WeiBo")
    for (id,weibocontent) in resList:
        print str(weibocontent).decode("utf8")

if __name__ == '__main__':
    main()