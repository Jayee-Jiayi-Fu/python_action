'''01．什么是抽象
抽象就是一种选择特征、简化认知的手段
'''

'''02．抽象与软件开发
- 人们广泛使用了抽象能力，并围绕抽象发明了许多概念和理论，分层思想就是其中最重要的概念之一
- 分层就在设计一个复杂系统时，按照问题抽象程度的高低，将系统划分为不同的抽象层
- 低级的抽象层里包含较多的实现细节。随着层级变高，细节越来越少，越接近我们想要解决的实际问题。
- 在这种分层结构下，每一层抽象都只依赖比它抽象级别更低的层，同时对比它抽象级别更高的层一无所知。因此，每层都可以脱离更高级别的层独立工作


分层是一种特别有用的设计理念。基于分层，我们可以把复杂系统的诸多细节封装到各个独立的抽象层中，每一层只关注特定内容，复杂度得到大大降低，系统也变得更容易理解。


- 即便是在非常微观的层面上，比如编写一个函数时，我们同样需要考虑函数内代码与抽象级别的关系。
- 假如一个函数内同时包含了多个抽象级别的内容，就会引发一系列的问题
'''
