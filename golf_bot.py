#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:32:32 2020

@author: daniel.kwon
"""


import sqlite3 as sql # to create the database

#===================#
#- creating tables -#
#===================#
conn = sql.connect('tee_time.db')

c = conn.cursor()

#Note: only need to run this once to initialize sqlite database
#c.execute('''CREATE TABLE tee_times
#          (datetime text, course_name text, golfer_name text)''')

#========================#
#- delete old tee times -#
#========================#
c.execute('''DELETE FROM tee_times WHERE date(datetime) < date('now')''')
for row in c.execute('''SELECT * FROM tee_times WHERE date(datetime) > date('2020-08-07')'''):
    print(row)
    
#====================#
#- insert tee times -#
#====================#
new_tee_time = ('','','')

c.execute('INSERT INTO tee_times VALUES (?,?,?)', new_tee_time)

#=======================#
#- print all tee times -#
#=======================#
for row in c.execute('''SELECT * FROM tee_times'''):
    print(row)

#===========================#
#- print any next tee time -#
#===========================#
for row in c.execute('''WITH ranked_list AS (
                            SELECT 
                                t.*
                                ,RANK() OVER(ORDER BY datetime) rank
                            FROM tee_times t)
                        SELECT 
                            datetime
                            ,course_name
                            ,golfer_name
                        FROM ranked_list WHERE rank=1'''):
                            print(row)

#==========================#
#- print my next tee time -#
#==========================#
for row in c.execute('''WITH ranked_list AS (
                            SELECT 
                                t.*
                                ,RANK() OVER(PARTITION BY golfer_name ORDER BY datetime) rank
                            FROM tee_times t)
                        SELECT 
                            datetime
                            ,course_name
                            ,golfer_name
                        FROM ranked_list 
                        WHERE rank=1
                        AND golfer_name='Dan'
                        '''):
                            print(row)
#=======================================#
#- commit changes and close connection -#
#=======================================#
conn.commit()

conn.close()