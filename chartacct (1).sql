-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 12, 2020 at 09:11 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chartacct`
--

-- --------------------------------------------------------

--
-- Table structure for table `chart_acct`
--

CREATE TABLE `chart_acct` (
  `id` int(10) NOT NULL,
  `aid` varchar(10) NOT NULL COMMENT 'accountant_id',
  `cid` varchar(10) NOT NULL COMMENT 'client_id'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chart_acct`
--

INSERT INTO `chart_acct` (`id`, `aid`, `cid`) VALUES
(2, '0', '0'),
(3, '0', '0'),
(4, '', 'not select'),
(39, '49', '25'),
(116, '57', '36'),
(149, '63', '31'),
(150, '57', '28'),
(151, '61', '28'),
(152, '64', '34'),
(153, '60', '30'),
(154, '62', '30'),
(155, '62', '35'),
(156, '63', '35'),
(157, '64', '35'),
(158, '60', '33'),
(159, '61', '33'),
(160, '63', '32'),
(161, '57', '26'),
(162, '58', '26'),
(163, '60', '26'),
(164, '61', '26'),
(165, '64', '26'),
(166, '65', '26'),
(169, '60', '37'),
(170, '58', '27'),
(171, '60', '27'),
(172, '61', '27'),
(173, '62', '27'),
(174, '65', '27'),
(175, '58', '29'),
(176, '62', '29'),
(177, '63', '29');

-- --------------------------------------------------------

--
-- Table structure for table `file_record`
--

CREATE TABLE `file_record` (
  `id` int(10) NOT NULL,
  `upload_by` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `datee` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `file` varchar(100) NOT NULL,
  `tag` varchar(100) NOT NULL,
  `type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `file_record`
--

INSERT INTO `file_record` (`id`, `upload_by`, `user_id`, `datee`, `file`, `tag`, `type`) VALUES
(1, 1, 61, '2020-02-29 04:01:47', '1000-06_06_2016 Btech IT 2012.pdf', '', 'admin'),
(2, 1, 61, '2020-02-29 04:01:47', '1000-78868b14-70c2-4305-9482-659782710567.pdf', '', 'admin'),
(3, 1, 61, '2019-03-01 04:02:11', '1000-06_06_2016 Btech IT 2012.pdf', '', 'admin'),
(4, 1, 61, '2020-02-29 04:02:11', '1000-78868b14-70c2-4305-9482-659782710567.pdf', '', 'admin'),
(5, 1, 55, '2020-02-29 04:03:56', '1000-3rd.pdf', '', 'admin'),
(6, 1, 55, '2020-02-29 04:03:57', '1000-4th.pdf', '', 'admin'),
(7, 1, 61, '2020-02-29 04:44:49', '1000-5th.pdf', '', 'admin'),
(8, 1, 84, '2020-02-29 22:48:04', '1000-ajavanotes.docx', '', 'admin'),
(9, 55, 55, '2020-02-29 22:52:35', '1000-ajavanotes.docx', '', 'client'),
(10, 1, 98, '2019-03-29 22:01:29', '1000-06_06_2016 Btech IT 2012.pdf', '', 'admin'),
(11, 1, 98, '2019-03-29 22:01:29', '1000-78868b14-70c2-4305-9482-659782710567.pdf', '', 'admin'),
(12, 45, 56, '2020-03-01 00:43:38', '1000-CC tut.docx', '', 'accountant'),
(13, 45, 56, '2020-03-03 04:12:45', '1000-admitcard.pdf', 'gst', 'accountant'),
(14, 47, 60, '2020-03-03 04:26:51', '1000-Cv.docx', 'gst,tax', 'accountant'),
(15, 47, 60, '2020-03-03 04:26:51', '1000-haa.png', 'gst,tax', 'accountant'),
(16, 47, 89, '2020-03-03 05:18:02', '1000-DT20195217456_Application.pdf', 'tax,gst2020', 'accountant'),
(17, 1, 55, '2020-03-09 21:13:20', '1000-gpic.jpg', '', 'admin'),
(18, 69, 69, '2020-04-30 09:51:37', 'flask_cheatsheet.pdf', 'tax-2020', 'client'),
(19, 69, 69, '2020-04-30 09:51:37', '1000-ajavanotes (22).docx', 'tax-2020', 'client'),
(20, 1, 71, '2020-04-30 10:32:59', 'DT20195217456_BGC_Form (1).pdf', 'tax-04', 'admin'),
(21, 1, 71, '2020-04-30 10:32:59', '1000-CC tut.docx', 'tax-04', 'admin'),
(22, 1, 98, '2020-04-30 10:35:32', 'DT20195217456_BGC_Form (1).pdf', 'gst-04', 'admin'),
(23, 1, 89, '2020-04-30 10:38:11', '1000-ajavanotes (23).docx', 'gst-20', 'admin'),
(24, 1, 89, '2020-04-30 10:38:11', '287721_119854_5925964 (1).pdf', 'gst-20', 'admin'),
(25, 86, 84, '2020-04-30 10:54:00', 'BEA1.docx', 'tax-04', 'accountant');

-- --------------------------------------------------------

--
-- Table structure for table `formacc`
--

CREATE TABLE `formacc` (
  `id` int(10) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `experience` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `type` varchar(20) NOT NULL,
  `user_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `formacc`
--

INSERT INTO `formacc` (`id`, `fname`, `lname`, `gender`, `experience`, `email`, `phone`, `type`, `user_id`) VALUES
(57, 'Raju', 'Chabara', 'Male', '2', 'acc21@gmail.com', '7896585960', 'accountant', 44),
(58, 'Amit', 'Girdhar', 'Male', '12', 'acc22@gmail.com', '4455226633', 'accountant', 45),
(60, 'Sumit', 'Girdhar', 'Male', '12', 'acc24@gmail.com', '4455226632', 'accountant', 47),
(61, 'Paras', 'Gupta', 'Male', '1', 'acc25@gmail.com', '8528528520', 'accountant', 57),
(62, 'Ojas', 'Arora', 'Male', '1', 'acc26@gmail.com', '1010101010', 'accountant', 59),
(63, 'Vibha', 'Arora', 'Female', '3', 'acc27@gmail.com', '6933963500', 'accountant', 86),
(64, 'Ram', 'Sharma', 'Male', '1', 'acc29@gmail.com', '8935350000', 'accountant', 99),
(65, 'Paras', 'Monga', 'Male', '3', 'acc33@gmail.com', '2839641700', 'acountant', 100);

-- --------------------------------------------------------

--
-- Table structure for table `formcli`
--

CREATE TABLE `formcli` (
  `id` int(10) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `company` varchar(50) NOT NULL,
  `gst` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `type` varchar(20) NOT NULL,
  `user_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `formcli`
--

INSERT INTO `formcli` (`id`, `fname`, `lname`, `gender`, `company`, `gst`, `email`, `phone`, `type`, `user_id`) VALUES
(26, 'Sunny', 'Sharma', 'Male', 'Kdsjhdslkjajajd', '27AASCS2ASQWE13', 'test@gmail.com', '1111111111', 'client', 55),
(27, 'Vikas', 'Kumra', 'Male', 'W3sols web development', '27AASCS2ASQWE14', 'test2@gmail.com', '1234567890', 'client', 56),
(28, 'Paras', 'Monga', 'Male', 'Kdsjhdslkjajajd', '27AASCS2ASQWE32', 'test3@gmail.com', '7478574103', 'client', 60),
(29, 'Rohit', 'Sharma', 'Male', 'Kdsjhdslkjajajd', '27AASCS2CXQWE25', 'test4@gmail.com', '3236353410', 'client', 61),
(30, 'Raju', 'Monga', 'Male', 'Njnvjwn gojrwn', '27AASCS2ASQWE60', 'test7@gmail.com', '2015013440', 'client', 69),
(31, 'Nanu', 'Sharma', 'Male', 'Kdsjhdslkjajajd', '27AASCS2CXQWE64', 'test8@gmail.com', '6324921650', 'client', 71),
(32, 'Sham', 'Sharma', 'Male', 'Kdsjhdslkjajajd', '27AASCS2ASQWE34', 'test11@gmail.com', '8501305106', 'client', 84),
(33, 'Riya', 'Kapoor', 'Female', 'W3sols web development', '27AASCM2CXQWE42', 'test28@gmail.com', '9685741200', 'client', 89),
(34, 'Paras', 'Monga', 'Male', 'Test address', 'AD23343469121ZE', 'paras@gmail.com', '9898989898', 'client', 97),
(35, 'Neelam', 'Girdhar', 'Female', 'Kdsjhdslkjajajd', '27AASCS2ASQWE36', 'test29@gmail.com', '1346782555', 'client', 98),
(36, 'Rajeev', 'Monga', 'male', 'Alpha Technology', '06AFSPM4441G1ZA', 'rajeevmonga@yahoo.com', '9812042279', 'client', 0),
(37, 'Savita', 'Monga', 'Female', 'Harton skill center', '27AASCS2ASWWE34', 'test31@gmail.com', '1111100000', 'client', 102);

-- --------------------------------------------------------

--
-- Table structure for table `logindb`
--

CREATE TABLE `logindb` (
  `id` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `key_gen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `logindb`
--

INSERT INTO `logindb` (`id`, `email`, `password`, `type`, `fname`, `lname`, `key_gen`) VALUES
(1, 'prs@gmail.com', '87985799d410ead3564453e2d9371ad5', 'admin', 'PARAS', 'MONGA', ''),
(44, 'acc21@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'accountant', 'Raju', 'Chabara', ''),
(45, 'acc22@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'accountant', 'Amit', 'Girdhar', ''),
(47, 'acc24@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'accountant', 'Sumit', 'Girdhar', ''),
(55, 'test@gmail.com', '08af7c3e82d6b1975d7f16ff1bac9abf', 'client', 'Sunny', 'Sharma', ''),
(56, 'test2@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'client', 'Vikas', 'Kumra', ''),
(57, 'acc25@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'accountant', 'Paras', 'Gupta', ''),
(59, 'acc26@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'accountant', 'Ojas', 'Arora', ''),
(60, 'test3@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'client', 'Paras', 'Monga', ''),
(61, 'test4@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'client', 'Rohit', 'Sharma', ''),
(69, 'test7@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'client', 'Raju', 'Monga', ''),
(71, 'test8@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'client', 'Nanu', 'Sharma', ''),
(84, 'test11@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'client', 'Sham', 'Sharma', ''),
(86, 'acc27@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'accountant', 'Vibha', 'Arora', ''),
(89, 'test28@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'client', 'Riya', 'Kapoor', ''),
(97, 'paras@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'client', 'Paras', 'Monga', ''),
(98, 'test29@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'client', 'Neelam', 'Girdhar', ''),
(99, 'acc29@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'accountant', 'Ram', 'Sharma', ''),
(100, 'acc33@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'accountant', 'Paras', 'Monga', ''),
(102, 'test31@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'client', 'Savita', 'Monga', '');

-- --------------------------------------------------------

--
-- Table structure for table `requestform`
--

CREATE TABLE `requestform` (
  `id` int(10) NOT NULL,
  `sender` varchar(100) NOT NULL COMMENT 'login_id',
  `reciever` varchar(100) NOT NULL COMMENT 'login_id',
  `subject` varchar(100) NOT NULL,
  `datee` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `message` longtext NOT NULL,
  `files` varchar(100) NOT NULL,
  `status` int(10) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `requestform`
--

INSERT INTO `requestform` (`id`, `sender`, `reciever`, `subject`, `datee`, `message`, `files`, `status`) VALUES
(137, '1', '55', 'ppppppppppppppppppp', '0000-00-00 00:00:00', 'ppppppppppppppppppp', '1000-2nd.pdf', 0),
(138, '1', '56', 'ppppppppppppppppppp', '0000-00-00 00:00:00', 'ppppppppppppppppppp', '1000-2nd.pdf', 0),
(139, '1', '25', 'ppppppppppppppppppp', '0000-00-00 00:00:00', 'ppppppppppppppppppp', '1000-2nd.pdf', 0),
(140, '1', '26', 'ppppppppppppppppppp', '0000-00-00 00:00:00', 'ppppppppppppppppppp', '1000-2nd.pdf', 0),
(141, '60', '1', 'saafas a  ', '2020-02-27 17:27:33', 'adbsz zb  z nzs  ', '1000-5th.pdf', 1),
(142, '60', '28', 'saafas a  ', '0000-00-00 00:00:00', 'adbsz zb  z nzs  ', '1000-5th.pdf', 0),
(143, '60', '33', 'saafas a  ', '0000-00-00 00:00:00', 'adbsz zb  z nzs  ', '1000-5th.pdf', 0),
(144, '99', '1', 'filesss', '2020-05-08 11:48:22', 'senddd dataaa', '1000-06_06_2016 Btech IT 2012.pdf', 1),
(145, '99', '0', 'filesss', '2020-02-26 04:41:31', 'senddd dataaa', '1000-06_06_2016 Btech IT 2012.pdf', 0),
(146, '99', '97', 'filesss', '2020-02-26 04:41:31', 'senddd dataaa', '1000-06_06_2016 Btech IT 2012.pdf', 0),
(147, '99', '98', 'filesss', '2020-02-26 04:41:31', 'senddd dataaa', '1000-06_06_2016 Btech IT 2012.pdf', 0),
(148, '84', '1', 'documentss', '2020-02-27 17:21:46', 'asfgafsgsfgfgf', '1000-ajavanotes.docx', 0),
(149, '84', '43', 'documentss', '2020-02-27 00:49:37', 'asfgafsgsfgfgf', '1000-ajavanotes.docx', 0),
(150, '84', '86', 'documentss', '2020-02-27 00:49:37', 'asfgafsgsfgfgf', '1000-ajavanotes.docx', 0),
(151, '89', '1', 'saafas a  ', '2020-02-27 17:26:51', 'to the shn ', '1000-CC tut.docx', 0),
(152, '89', '57', 'saafas a  ', '2020-02-27 00:58:31', 'to the shn ', '1000-CC tut.docx', 0),
(153, '55', '1', 'Tax-2020', '2020-05-08 08:06:43', 'All records of tax-2020', '287721_119854_5925964.pdf', 0),
(154, '55', '58', 'Tax-2020', '2020-04-28 10:02:04', 'All records of tax-2020', '287721_119854_5925964.pdf', 0),
(155, '55', '61', 'Tax-2020', '2020-04-28 10:02:10', 'All records of tax-2020', '287721_119854_5925964.pdf', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chart_acct`
--
ALTER TABLE `chart_acct`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `file_record`
--
ALTER TABLE `file_record`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `formacc`
--
ALTER TABLE `formacc`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `phone` (`phone`),
  ADD UNIQUE KEY `email` (`email`(20));

--
-- Indexes for table `formcli`
--
ALTER TABLE `formcli`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `gst` (`gst`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `phone` (`phone`);

--
-- Indexes for table `logindb`
--
ALTER TABLE `logindb`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `requestform`
--
ALTER TABLE `requestform`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chart_acct`
--
ALTER TABLE `chart_acct`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=178;

--
-- AUTO_INCREMENT for table `file_record`
--
ALTER TABLE `file_record`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `formacc`
--
ALTER TABLE `formacc`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `formcli`
--
ALTER TABLE `formcli`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `logindb`
--
ALTER TABLE `logindb`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- AUTO_INCREMENT for table `requestform`
--
ALTER TABLE `requestform`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=156;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
