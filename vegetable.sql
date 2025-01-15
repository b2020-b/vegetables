/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80039
 Source Host           : localhost:3306
 Source Schema         : vegetable

 Target Server Type    : MySQL
 Target Server Version : 80039
 File Encoding         : 65001

 Date: 15/01/2025 15:26:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sales
-- ----------------------------
DROP TABLE IF EXISTS `sales`;
CREATE TABLE `sales`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `vegetable_id` int NULL DEFAULT NULL,
  `quantity` int NOT NULL,
  `sale_date` date NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `vegetable_id`(`vegetable_id`) USING BTREE,
  CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`vegetable_id`) REFERENCES `vegetables` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sales
-- ----------------------------
INSERT INTO `sales` VALUES (3, 3, 4, '2025-01-15');
INSERT INTO `sales` VALUES (4, 3, 5, '2025-01-15');
INSERT INTO `sales` VALUES (5, 3, 1, '2025-01-15');
INSERT INTO `sales` VALUES (6, 4, 3, '2025-01-15');
INSERT INTO `sales` VALUES (7, 5, 30, '2025-01-15');
INSERT INTO `sales` VALUES (8, 6, 2, '2025-01-15');
INSERT INTO `sales` VALUES (9, 7, 4, '2025-01-15');

-- ----------------------------
-- Table structure for vegetables
-- ----------------------------
DROP TABLE IF EXISTS `vegetables`;
CREATE TABLE `vegetables`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` decimal(10, 2) NOT NULL,
  `create_time` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of vegetables
-- ----------------------------
INSERT INTO `vegetables` VALUES (3, '萝卜', 6.00, '2025-01-15 14:59:33');
INSERT INTO `vegetables` VALUES (4, '苹果', 7.54, '2025-01-15 15:05:30');
INSERT INTO `vegetables` VALUES (5, '西红柿', 4.69, '2025-01-15 15:11:15');
INSERT INTO `vegetables` VALUES (6, '芹菜', 6.00, '2025-01-15 15:16:31');
INSERT INTO `vegetables` VALUES (7, '大白菜', 0.99, '2025-01-15 15:22:04');

SET FOREIGN_KEY_CHECKS = 1;
