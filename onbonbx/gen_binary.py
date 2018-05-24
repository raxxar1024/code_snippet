# -*- coding: utf-8 -*-
# 偏移    字段                  长度          默认值     描述
# 0x0000  FileType              2           0x8000  文件类型（0x8000 ORD 文件）
# 0x0002  Version               1           0x10    文件定义版本号
# 0x0003  Reserved              61          0x00    保留字
# 0x0040  PreviewWidth          2           0x0000  预览图参考宽度
# 0x0042  PreviewHeight         2           0x0000  预览图参考高度
# 0x0044  BlockCount            2           0x0000  光带段数
# 0x0046  Reserved              10          0x00    保留字
# 0x0050  Reserved              48          0x00    保留字

# 0x0080  Block0 PixCount       2           0x01,0x00  Block0 像素点数
# 0x0082  Block0 DefaultColor   3           R,G,B  Block0 默认颜色
# 0x0085  Reserved              11          0x00    保留字
# 0x0090  Block0Data            N           0x01,0x00  可变 Block0 像素点数
# 其它 Block 数据
#         FileCrc               4           0x00  前面所有数据的和较验



import struct

table = [
    0X0000, 0XC0C1, 0XC181, 0X0140, 0XC301, 0X03C0, 0X0280, 0XC241,
    0XC601, 0X06C0, 0X0780, 0XC741, 0X0500, 0XC5C1, 0XC481, 0X0440,
    0XCC01, 0X0CC0, 0X0D80, 0XCD41, 0X0F00, 0XCFC1, 0XCE81, 0X0E40,
    0X0A00, 0XCAC1, 0XCB81, 0X0B40, 0XC901, 0X09C0, 0X0880, 0XC841,
    0XD801, 0X18C0, 0X1980, 0XD941, 0X1B00, 0XDBC1, 0XDA81, 0X1A40,
    0X1E00, 0XDEC1, 0XDF81, 0X1F40, 0XDD01, 0X1DC0, 0X1C80, 0XDC41,
    0X1400, 0XD4C1, 0XD581, 0X1540, 0XD701, 0X17C0, 0X1680, 0XD641,
    0XD201, 0X12C0, 0X1380, 0XD341, 0X1100, 0XD1C1, 0XD081, 0X1040,
    0XF001, 0X30C0, 0X3180, 0XF141, 0X3300, 0XF3C1, 0XF281, 0X3240,
    0X3600, 0XF6C1, 0XF781, 0X3740, 0XF501, 0X35C0, 0X3480, 0XF441,
    0X3C00, 0XFCC1, 0XFD81, 0X3D40, 0XFF01, 0X3FC0, 0X3E80, 0XFE41,
    0XFA01, 0X3AC0, 0X3B80, 0XFB41, 0X3900, 0XF9C1, 0XF881, 0X3840,
    0X2800, 0XE8C1, 0XE981, 0X2940, 0XEB01, 0X2BC0, 0X2A80, 0XEA41,
    0XEE01, 0X2EC0, 0X2F80, 0XEF41, 0X2D00, 0XEDC1, 0XEC81, 0X2C40,
    0XE401, 0X24C0, 0X2580, 0XE541, 0X2700, 0XE7C1, 0XE681, 0X2640,
    0X2200, 0XE2C1, 0XE381, 0X2340, 0XE101, 0X21C0, 0X2080, 0XE041,
    0XA001, 0X60C0, 0X6180, 0XA141, 0X6300, 0XA3C1, 0XA281, 0X6240,
    0X6600, 0XA6C1, 0XA781, 0X6740, 0XA501, 0X65C0, 0X6480, 0XA441,
    0X6C00, 0XACC1, 0XAD81, 0X6D40, 0XAF01, 0X6FC0, 0X6E80, 0XAE41,
    0XAA01, 0X6AC0, 0X6B80, 0XAB41, 0X6900, 0XA9C1, 0XA881, 0X6840,
    0X7800, 0XB8C1, 0XB981, 0X7940, 0XBB01, 0X7BC0, 0X7A80, 0XBA41,
    0XBE01, 0X7EC0, 0X7F80, 0XBF41, 0X7D00, 0XBDC1, 0XBC81, 0X7C40,
    0XB401, 0X74C0, 0X7580, 0XB541, 0X7700, 0XB7C1, 0XB681, 0X7640,
    0X7200, 0XB2C1, 0XB381, 0X7340, 0XB101, 0X71C0, 0X7080, 0XB041,
    0X5000, 0X90C1, 0X9181, 0X5140, 0X9301, 0X53C0, 0X5280, 0X9241,
    0X9601, 0X56C0, 0X5780, 0X9741, 0X5500, 0X95C1, 0X9481, 0X5440,
    0X9C01, 0X5CC0, 0X5D80, 0X9D41, 0X5F00, 0X9FC1, 0X9E81, 0X5E40,
    0X5A00, 0X9AC1, 0X9B81, 0X5B40, 0X9901, 0X59C0, 0X5880, 0X9841,
    0X8801, 0X48C0, 0X4980, 0X8941, 0X4B00, 0X8BC1, 0X8A81, 0X4A40,
    0X4E00, 0X8EC1, 0X8F81, 0X4F40, 0X8D01, 0X4DC0, 0X4C80, 0X8C41,
    0X4400, 0X84C1, 0X8581, 0X4540, 0X8701, 0X47C0, 0X4680, 0X8641,
    0X8201, 0X42C0, 0X4380, 0X8341, 0X4100, 0X81C1, 0X8081, 0X4040
]


def CRC(crc, byte):
    lower = crc >> 8
    return (lower ^ table[((crc) ^ (byte & 0xffffffff)) & 0xff])


def CalcCRC(data, size):
    crc = 0
    for i in xrange(size):
        crc = CRC(crc, data[i])
    return crc


def getFileCRC(_path, block_size):
    f = open(_path, "rb")
    read_data = f.read(block_size)
    f.close()
    read_data_arr = [ord(c) for c in read_data]
    return CalcCRC(read_data_arr, block_size)


def get_checksum(_path, block_size):
    f = open(_path, "rb")
    read_data = f.read(block_size)
    f.close()
    read_data_arr = [ord(c) for c in read_data]
    return sum(read_data_arr)


def gen_file_1st(file_name, dict_para):
    WriteFileData = open(file_name, 'wb')

    FileType = 0x8000
    WriteFileData.write(struct.pack("H", FileType))

    Version = 0x10
    WriteFileData.write(struct.pack("B", Version))

    Reserved = 0x00
    for i in xrange(61):
        WriteFileData.write(struct.pack("B", Reserved))

    PreviewWidth = 128
    WriteFileData.write(struct.pack("H", PreviewWidth))

    PreviewHeight = 96
    WriteFileData.write(struct.pack("H", PreviewHeight))

    BlockCount = 0x1
    WriteFileData.write(struct.pack("H", BlockCount))

    Reserved = 0x00
    for i in xrange(10 + 48):
        WriteFileData.write(struct.pack("B", Reserved))

    Block0_PixCount = dict_para["w"] * dict_para["h"]
    WriteFileData.write(struct.pack("H", Block0_PixCount))

    DefaultColor_R = dict_para["r"]
    WriteFileData.write(struct.pack("B", DefaultColor_R))
    DefaultColor_G = dict_para["g"]
    WriteFileData.write(struct.pack("B", DefaultColor_G))
    DefaultColor_B = dict_para["b"]
    WriteFileData.write(struct.pack("B", DefaultColor_B))

    Reserved = 0x00
    for i in xrange(11):
        WriteFileData.write(struct.pack("B", Reserved))

    for i in xrange(dict_para["y"], dict_para["y"] + dict_para["h"]):
        for j in xrange(dict_para["x"], dict_para["x"] + dict_para["w"]):
            WriteFileData.write(struct.pack("H", j))
            WriteFileData.write(struct.pack("H", i))

    WriteFileData.close()


def gen_file(file_name, dict_para):
    gen_file_1st(file_name, dict_para)
    file_size = os.path.getsize(file_name)
    check_sum = get_checksum(file_name, file_size) & 0xffffffff

    WriteFileData = open(file_name, 'a')
    WriteFileData.write(struct.pack("I", check_sum))
    WriteFileData.close()


if __name__ == "__main__":
    # file_name = 'R001'
    # gen_file_1st(file_name, R_color=0xff, G_color=0x00, B_color=0x00)
    #
    # check_sum = get_checksum(file_name, 0xc090) & 0xffffffff
    # crc = getFileCRC(file_name, 0xc090)
    #
    # WriteFileData = open(file_name, 'a')
    # WriteFileData.write(struct.pack("I", check_sum))
    # WriteFileData.close()
    #
    # file_name = 'R002'
    # gen_file_1st(file_name, R_color=0x00, G_color=0xff, B_color=0x00)
    #
    # check_sum = get_checksum(file_name, 0xc090) & 0xffffffff
    # crc = getFileCRC(file_name, 0xc090)
    #
    # WriteFileData = open(file_name, 'a')
    # WriteFileData.write(struct.pack("I", check_sum))
    # WriteFileData.close()
    import os

    dict_para = {
        "x": 112, "y": 0, "w": 8, "h": 96, "r": 0xff, "g": 0x00, "b": 0x00
    }
    gen_file('R003', dict_para)
    dict_para = {
        "x": 112, "y": 0, "w": 8, "h": 96, "r": 0x00, "g": 0xff, "b": 0x00
    }
    gen_file('R004', dict_para)
    dict_para = {
        "x": 120, "y": 0, "w": 8, "h": 96, "r": 0xff, "g": 0x00, "b": 0x00
    }
    gen_file('R005', dict_para)
    dict_para = {
        "x": 120, "y": 0, "w": 8, "h": 96, "r": 0x00, "g": 0xff, "b": 0x00
    }
    gen_file('R006', dict_para)
