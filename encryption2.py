# mat = [[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,3,7]]
# c=0
# x=0
# y=0
# for i in range(0,4):
#     for j in range(0,3):
#         if j == 0:
#             if mat[i][j] == mat[i][j+1] or mat[i][j] == mat[i][j+2] or mat[i][j] == mat[i][j+3]:
#                 c = c+1
#                 break
#         if j == 1:
#             if mat[i][j] == mat[i][j+1] or mat[i][j] == mat[i][j+2]:
#                 x = x+1
#                 break
#         if j == 2:
#             if mat[i][j] == mat[i][j+1]:
#                 y = y+1
#                 break
#         if j == 3:
#             break
# print(c+x+y)




#
# from subprocess import check_output
# out = check_output(("netsh wlan show profiles"), shell=True)
# def wifi_network_name(out):
#     File=[]
#     for i in range (len(out)):
#           File.append(chr(out[i]))
#     data = ""
#     for j in File:
#         if j != "":
#             data = data+j
#     File =[]
#     File.append(data.replace("\r\n",""))
#     a = File[0]
#     b = list(map(str, a.split("All User Profile     :")))
#     File = []
#     for i in b[2::]:
#         File.append(i.replace(" ","*"))
#     return File
# comm = wifi_network_name(out)
# File = []
# for i in comm:
#     File.append("netsh wlan show profiles "+i+" key=clear")
# print(File)




















