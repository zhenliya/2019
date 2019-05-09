# vue 获取dom元素

var el = event.target; //当前元素，可修改（能够用此方法获取到他的子元素，不能获取他本身的内容） 
var el = event.currentTarget;//当前元素，不可修改（能够用此方法获取到他的子元素及能获取他本身的内容）


```vue.js

<button @click = “clickfun($event)”>点击</button>
 
methods: {
clickfun(e) {
// e.target 是你当前点击的元素
// e.currentTarget 是你绑定事件的元素
    #获得点击元素的前一个元素
    e.currentTarget.previousElementSibling.innerHTML
    #获得点击元素的第一个子元素
    e.currentTarget.firstElementChild
    # 获得点击元素的下一个元素
    e.currentTarget.nextElementSibling
    # 获得点击元素中id为string的元素
    e.currentTarget.getElementById("string")
    # 获得点击元素的string属性
    e.currentTarget.getAttributeNode('string')
    # 获得点击元素的父级元素
    e.currentTarget.parentElement
    # 获得点击元素的前一个元素的第一个子元素的HTML值
    e.currentTarget.previousElementSibling.firstElementChild.innerHTML
    获取所有子元素
    e.target.childList
    e.target.childElementCount
 
    }

};

```