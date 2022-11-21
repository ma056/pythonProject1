# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : mysql平时用法.py
@Author : wenjing
@Date : 2022/11/18 14:46


"""
'''
一、插入时重复处理
1、重复条件
    字段为主键、唯一键
2、重复处理方式
    重复时不插入（ignore）、重复时删除重建（replace into）、重复时更新（on duplicate key update）
3、应用场合
    重复时更新：存在更新，不存在插入


'''
'''
二、测试
1、建表
CREATE TABLE `person` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `NAME` varchar(32) DEFAULT NULL,
  `age` int unsigned DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `birthday` datetime DEFAULT CURRENT_TIMESTAMP,
  `class` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lindex_person_name` (`NAME`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

2、创建唯一索引
-- 创建唯一索引
ALTER TABLE person ADD UNIQUE INDEX lindex_person_name USING BTREE (`name`);
-- 删除索引
-- ALTER TABLE person DROP INDEX lindex_person_name;
3、插入数据
3.1重复时更新旧数据
-- 重复时更新
-- 重复时仅更新 ON DUPLICATE KEY UPDATE 后面的字段，其它字段都不更新
INSERT INTO `test`.`person`(`name`, `age`, `sex`, `birthday`, `class`) VALUES 
('lilisss', 100, 'c', '2001-01-02 00:00:00', 2)
ON DUPLICATE KEY UPDATE  name = CONCAT(values(name), '_'), age = values(age) + 20;
 
-- 重复时用新记录覆盖旧记录
INSERT INTO `test`.`person`(`name`, `age`, `sex`, `birthday`, `class`) VALUES 
('lili', 19, 'c', '2001-01-02 00:00:00', 2)
ON DUPLICATE KEY UPDATE  name = values(name), age = values(age), sex = values(sex), birthday = values(birthday), class = values (class);


3.2重复时，不插入新纪录
-- 重复时不插入
INSERT IGNORE INTO `test`.`person`(`name`, `age`, `sex`, `birthday`, `class`) VALUES 
('lili', 19, 'm', '2001-01-02 00:00:00', 2);
 
-- 重复时删除重建
-- 删除原语句，插入新语句
REPLACE INTO `test`.`person`(`name`, `age`, `sex`, `birthday`, `class`) VALUES 
('lilissssss', 19, 's', '2001-01-02 00:00:00', 2);

3.3重复时，删除旧纪录，插入新记录
-- 重复时删除重建
-- 删除原语句，插入新语句
REPLACE INTO `test`.`person`(`name`, `age`, `sex`, `birthday`, `class`) VALUES 
('lilissssss', 19, 's', '2001-01-02 00:00:00', 2);
replace into 'test'.'person'('name','age','sex','birthday','class') values('lilissssss', 19, 's', '2001-01-02 00:00:00', 2)
'''