# set
set1 = set()
set1 = {1,2,3,4,'w'}
# ���ֵ佨����{}�����Բ���ʹ��{}��ʾ�ռ���
'''
һЩ���� - | & ^
'''
set1.add(5)
set1.update(6)
# ������
set1.remove(6)  # ������KeyError�Ĵ���
set1.discard(6)  # ������������
set1.pop()  # ���ɾ��һ�� ����ɾ����Ԫ��

len(set1)
set1.clear()
2 in set1
# �ȵ�

