""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check(root,minv,maxv):
    if root is None: return True
    if root.data<=minv or root.data>=maxv:return False
    ans1=check(root.left,minv,root.data)
    ans2=check(root.right,root.data,maxv)
    ans=ans1 and ans2
    return ans
def check_binary_search_tree_(root):
    return check(root,-1,9999999999)