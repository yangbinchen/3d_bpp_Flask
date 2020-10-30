import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import seaborn as sns
import random
from .main import *

def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    cnames = ['#F0F8FF','#FAEBD7','#00FFFF','#7FFFD4','#F0FFFF','#F5F5DC','#FFE4C4','#000000','#FFEBCD',
              '#0000FF','#8A2BE2','#A52A2A','#DEB887','#5F9EA0','#7FFF00','#D2691E','#FF7F50','#6495ED',
              '#FFF8DC','#DC143C','#00FFFF','#00008B','#008B8B','#B8860B','#A9A9A9','#006400','#BDB76B',
              '#8B008B','#556B2F','#FF8C00','#9932CC','#8B0000','#E9967A','#8FBC8F','#483D8B','#2F4F4F',
              '#00CED1','#9400D3','#FF1493','#00BFFF','#696969','#1E90FF','#B22222','#FFFAF0','#228B22',
              '#FF00FF','#DCDCDC','#F8F8FF','#FFD700','#DAA520','#808080','#008000','#ADFF2F','#F0FFF0',
              '#FF69B4','#CD5C5C','#4B0082','#FFFFF0','#F0E68C','#E6E6FA','#FFF0F5','#7CFC00','#FFFACD',
              '#ADD8E6','#F08080','#E0FFFF','#FAFAD2','#90EE90','#D3D3D3','#FFB6C1','#FFA07A','#20B2AA',
              '#87CEFA','#778899','#B0C4DE','#FFFFE0','#00FF00','#32CD32','#FAF0E6','#FF00FF','#800000',
              '#66CDAA','#0000CD','#BA55D3','#9370DB','#3CB371','#7B68EE','#00FA9A','#48D1CC','#C71585',
              '#191970','#F5FFFA','#FFE4E1','#FFE4B5','#FFDEAD','#000080','#FDF5E6','#808000','#6B8E23',
              '#FFA500','#FF4500','#DA70D6','#EEE8AA','#98FB98','#AFEEEE','#DB7093','#FFEFD5','#FFDAB9',
              '#CD853F','#FFC0CB','#DDA0DD','#B0E0E6','#800080','#FF0000','#BC8F8F','#4169E1','#8B4513',
              '#FA8072','#FAA460','#2E8B57','#FFF5EE','#A0522D','#C0C0C0','#87CEEB','#6A5ACD','#708090',
              '#FFFAFA','#00FF7F','#4682B4','#D2B48C','#008080','#D8BFD8','#FF6347','#40E0D0','#EE82EE',
              '#F5DEB3''#FFFFFF','#F5F5F5','#FFFF00','#9ACD32']
    color = ""
    color += cnames[random.randint(0,100)]
    return color

def item_show(bin_x,bin_y,bin_z,items):
    # bin的长宽高，item的list
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # 四面体顶点和面
    for i in items:
        # 获得每个面的顶点
        verts = [(i[0][0], i[0][1], i[0][2]), (i[0][0], i[0][1]+i[2], i[0][2]), (i[0][0]+i[1], i[0][1]+i[2], i[0][2]),
                 (i[0][0]+i[1], i[0][1], i[0][2]), (i[0][0], i[0][1], i[0][2]+i[3]), (i[0][0], i[0][1]+i[2], i[0][2]+i[3]),
                 (i[0][0]+i[1], i[0][1]+i[2], i[0][2]+i[3]),(i[0][0]+i[1], i[0][1], i[0][2]+i[3])]
        faces = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [0, 3, 7, 4]]
        poly3d = [[verts[vert_id] for vert_id in face] for face in faces]
#         print(poly3d)
        # 绘制顶点
        x, y, z = zip(*verts)
        # 绘制多边形面
        ax.add_collection3d(Poly3DCollection(poly3d, facecolors=randomcolor(), linewidths=1, alpha=0.3))
        # 绘制对变形的边
        ax.add_collection3d(Line3DCollection(poly3d, colors='k', linewidths=0.5, linestyles=':'))
        # 设置图形坐标范围
    ax.set_xlabel('X')
    ax.set_xlim3d(0, bin_x)
    ax.set_ylabel('Y')
    ax.set_ylim3d(0, bin_y)
    ax.set_zlabel('Z')
    ax.set_zlim3d(0,bin_z)
    plt.title("3dbin_packing_show")
    plt.show()

#item_show(3, 3, 3, [((0, 0, 0), 1, 1, 1), ((0, 1, 0), 1, 1, 1)])



