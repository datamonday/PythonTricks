# 4. 以字典为基础建立一个通讯录，
#    向字典中添加和删除通讯人（名字、电话、email、工作单位等），查询某个人的信息，然后输出通讯录中所有人的信息。

class Concat:
    def __init__(self):
        self.dict = {}
        self.dict["name"] = []
        self.dict["phone"] = []
        self.dict["email"] = []
        self.dict["address"] = []
        
    def get_idx_by_name(self, target):
        """
        为了方便删除和查询信息，定义该函数实现根据name返回索引的功能
        """
        for idx, name in enumerate(self.dict['name']):
            if name == target:
                return idx
        
    def add(self, name, phone, email, address):
        # 防止重复添加
        if name not in self.dict["name"]:
            self.dict["name"].append(name)
            self.dict["phone"].append(phone)
            self.dict["email"].append(email)
            self.dict["address"].append(address)
        else:
            print(f"{name} information has existed!")
    
    def check(self, name):
        if name in self.dict["name"]:
            idx = self.get_idx_by_name(name)
            print("name:    ", self.dict["name"][idx])
            print("phone:   ", self.dict["phone"][idx])
            print("email:   ", self.dict["email"][idx])
            print("address: ", self.dict["address"][idx])
        else:
            print(f"None of {name} information!")
    
    def delete(self, name):
        if name in self.dict["name"]:
            idx = self.get_idx_by_name(name)
            del self.dict["name"][idx]
            del self.dict["phone"][idx]
            del self.dict["email"][idx]
            del self.dict["address"][idx]
            
        else:
            print(f"None of {name} information!")
    
    def show_all_info(self):
        for keys_values in zip(self.dict.items()):
            print(keys_values)
            
"""
concat = Concat()
concat.show_all_info()

(('name', []),)
(('phone', []),)
(('email', []),)
(('address', []),)

# ----------------------------------------------------------------------- # 
concat.add("messi", 10, "fcb_messi@fcb.com", "bacelona")
concat.show_all_info()

(('name', ['messi']),)
(('phone', [10]),)
(('email', ['fcb_messi@fcb.com']),)
(('address', ['bacelona']),)

# ----------------------------------------------------------------------- # 
concat.add("pedri", 16, "fcb_pedri@fcb.com", "bacelona")
concat.show_all_info()

(('name', ['messi', 'pedri']),)
(('phone', [10, 16]),)
(('email', ['fcb_messi@fcb.com', 'fcb_pedri@fcb.com']),)
(('address', ['bacelona', 'bacelona']),)

# ----------------------------------------------------------------------- # 
concat.add("dest", 2, "fcb_dest@fcb.com", "bacelona")
concat.show_all_info()

(('name', ['messi', 'pedri', 'dest']),)
(('phone', [10, 16, 2]),)
(('email', ['fcb_messi@fcb.com', 'fcb_pedri@fcb.com', 'fcb_dest@fcb.com']),)
(('address', ['bacelona', 'bacelona', 'bacelona']),)

# ----------------------------------------------------------------------- # 
concat.check("messi")

name:     messi
phone:    10
email:    fcb_messi@fcb.com
address:  bacelona

# ----------------------------------------------------------------------- # 
concat.delete("dest")
concat.show_all_info()

(('name', ['messi', 'pedri']),)
(('phone', [10, 16]),)
(('email', ['fcb_messi@fcb.com', 'fcb_pedri@fcb.com']),)
(('address', ['bacelona', 'bacelona']),)
"""