-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2026 at 10:06 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sokogardenonline`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(200) NOT NULL,
  `product_name` varchar(500) NOT NULL,
  `product_description` varchar(200) NOT NULL,
  `Product_cost` varchar(2000) NOT NULL,
  `product_photo` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `product_description`, `Product_cost`, `product_photo`) VALUES
(1, 'Android Smartphone', 'This is a very good phone', '25400', '<FileStorage: \'phone1.jfif\' (\'application/octet-stream\')>'),
(2, 'Iphone 16 ', 'This phonre id goodand fast', '54000', '<FileStorage: \'phone2.jfif\' (\'application/octet-stream\')>'),
(3, 'Android smartphone', 'This is a stylish phone', '17000', '<FileStorage: \'phone3.jfif\' (\'application/octet-stream\')>'),
(4, 'Android smartphone', 'This is a good phone', '20000', '<FileStorage: \'phone4.jfif\' (\'application/octet-stream\')>'),
(5, 'Android smartphone', 'This is a great phone', '20000', '<FileStorage: \'phone5.jfif\' (\'application/octet-stream\')>'),
(6, 'Android smartphone', 'This phone has good taste', '30000', '<FileStorage: \'phone6.jfif\' (\'application/octet-stream\')>'),
(10, 'Android smartphone', 'This phone has good taste', '30000', '<FileStorage: \'phone6.jfif\' (\'application/octet-stream\')>');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(50) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `email`, `phone`, `password`) VALUES
(1, 'Benson', 'Benso@gmail.com', '25489756412', '2546');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
