# -*- coding:utf-8 -*-
import os
from PIL import Image
def splitimage(src, rownum, colnum, dstpath):  # �ָ�ͼƬ
    img = Image.open(src)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('��ʼ����ͼƬ�и�, ���Ժ�...')

        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]

        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext), ext)
                num = num + 1

        print('ͼƬ�и���ϣ������� %s ��СͼƬ��' % num)
    else:
        print('���Ϸ��������и������')

if __name__ == '__main__':		
	src = input('������ͼƬ�ļ�·����')
	if os.path.isfile(src):
		dstpath = input('������ͼƬ���Ŀ¼��������·�����ʾʹ��ԴͼƬ����Ŀ¼����')
		if (dstpath == '') or os.path.exists(dstpath):
			row = int(input('�������и�������'))
			col = int(input('�������и�������'))
			if row > 0 and col > 0:
				splitimage(src, row, col, dstpath)
			else:
				print('��Ч�������и������')
		else:
			print('ͼƬ���Ŀ¼ %s �����ڣ�' % dstpath)
	else:
		print('ͼƬ�ļ� %s �����ڣ�' % src)