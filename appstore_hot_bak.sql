--
-- Database: `my_db`
--

-- --------------------------------------------------------

--
-- 表的结构 `appstore_hot_bak`
--

CREATE TABLE IF NOT EXISTS `appstore_hot_bak` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `name` varchar(256) DEFAULT NULL COMMENT '应用名称',
  `corp` varchar(256) DEFAULT NULL COMMENT '公司名称',
  `rank` int(8) NOT NULL DEFAULT '0' COMMENT '名次',
  `free` tinyint(4) NOT NULL DEFAULT '-1' COMMENT '1免费，0畅销',
  `type` tinyint(4) NOT NULL DEFAULT '-1' COMMENT '0总，1游戏，2娱乐',
  `date` date  COMMENT '日期',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='APP store实时热榜' AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
