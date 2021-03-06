# How Convolutional Neural Networks Work（2）

## 神经网络是怎样工作的（2）

*原视频地址：https://www.youtube.com/watch?v=FmpDIaiMIeA&t=51s*

*文字为个人理解和部分字幕翻译*

----------

**目录：**

神经网络是怎样工作的（1）

1. CNN概述

2. Convolution Layer (卷积层)

神经网络是怎样工作的（2）

3. Pooling Layer (池化层)

4. Normalization (标准化)

5. Fully Connected Layer (全连接层)

6. Layers Get Stacked (各层堆叠)

神经网络是怎样工作的（3）

7. Others (其他)

----------

### 3. Pooling Layer (池化层)

[![22.png](https://i.loli.net/2018/06/04/5b1537b709a16.png)](https://i.loli.net/2018/06/04/5b1537b709a16.png)

> 池化：缩减卷积层得到的过滤图
> 
> 1.选择一个窗口大小（通常是2或者3）
> 	
> 2.选择一个步幅（通常是2）
> 	
> 3.在过滤图上移动窗口
> 	
> 4.在每个窗口中选择最大值

我们用到的第二个技巧叫做池化（Pooling），用来缩减卷积层得到的过滤图，这个方法很直接，就在过滤图上移动选择好大小的窗口，在窗口中选择最大的值。

[![23.png](https://i.loli.net/2018/06/04/5b1537b3d003e.png)](https://i.loli.net/2018/06/04/5b1537b3d003e.png)

[![24.png](https://i.loli.net/2018/06/04/5b1537b60569b.png)](https://i.loli.net/2018/06/04/5b1537b60569b.png)

不断重复这个过程，我们得到一个与之前差不多但小一些的图，仍然可以看出匹配度高的部分分布在这个斜线上，而图片大小约为之前的一半。

缩减让之后的工作变得更容易。并且池化并不关心最大值出现在窗口的什么位置，可以降低图片像素位置的敏感度，当你分辨一个图片的时候，像素点左移一点右移一点或者旋转一点都不是那么重要。

[![25.png](https://i.loli.net/2018/06/04/5b1537b831214.png)](https://i.loli.net/2018/06/04/5b1537b831214.png)

我们对所有过滤得到的图进行池化。

[![26.png](https://i.loli.net/2018/06/04/5b1537b73e8ab.png)](https://i.loli.net/2018/06/04/5b1537b73e8ab.png)

### 4. Normalization (标准化)

[![27.png](https://i.loli.net/2018/06/04/5b154c6119680.png)](https://i.loli.net/2018/06/04/5b154c6119680.png)

> 标准化
> 
> 在不破坏数学特征的基础上对匹配值做一些改变。
> 
> 将负值改为0。

现在是另一个技巧——标准化（Normalization），我们要做的就是将图中所有的负值改为0。

[![28.png](https://i.loli.net/2018/06/04/5b1537b76e99d.png)](https://i.loli.net/2018/06/04/5b1537b76e99d.png)

[![29.png](https://i.loli.net/2018/06/04/5b1537b947ddf.png)](https://i.loli.net/2018/06/04/5b1537b947ddf.png)

最终你会得到一个和之前很相似的图，只是图中没有负数。

[![30.png](https://i.loli.net/2018/06/04/5b1537b843189.png)](https://i.loli.net/2018/06/04/5b1537b843189.png)

我们对每张图进行标准化，这就是CCN的另外一层。

[![31.png](https://i.loli.net/2018/06/04/5b154db451237.png)](https://i.loli.net/2018/06/04/5b154db451237.png)

神奇的地方就就在这里了，当我们把上面这三层组合起来，我们就可以得到经历过层与层堆叠之后的输出结果。

[![32.png](https://i.loli.net/2018/06/04/5b154db55e7bc.png)](https://i.loli.net/2018/06/04/5b154db55e7bc.png)

我们也可以任意次数地重复这个堆叠的结构，每次的卷积层得到过滤结果，池化层让过滤图更小。

### 5. Fully Connected Layer (全连接层)

[![33.png](https://i.loli.net/2018/06/04/5b154db37e2aa.png)](https://i.loli.net/2018/06/04/5b154db37e2aa.png)

我们CNN的最后一层，叫做全连接层。在这里每一个值都变成了一个指标，将决定这张图最终是X还是O。我们把它们排成一列，因为这样看起来更方便。

[![34.png](https://i.loli.net/2018/06/04/5b154db587008.png)](https://i.loli.net/2018/06/04/5b154db587008.png)

当我们将一个图片与X相匹配时，就会有一些位置的值应该大，证明这张图片很可能是X。
同理，O也有起决定性作用的位置。

[![35.png](https://i.loli.net/2018/06/04/5b154db5803f2.png)](https://i.loli.net/2018/06/04/5b154db5803f2.png)

当我们得到一张新的图片，不知道它是O还是X时，我们按照上述的步骤得到这样的一维矩阵，可以看出，在X的决定性位置它的匹配度平均值为0.92，而O决定性位置的匹配度平均值为0.51，所以这张图很有可能是X。

[![36.png](https://i.loli.net/2018/06/04/5b154db3da606.png)](https://i.loli.net/2018/06/04/5b154db3da606.png)

[![37.png](https://i.loli.net/2018/06/04/5b154db3c8bb8.png)](https://i.loli.net/2018/06/04/5b154db3c8bb8.png)

有趣的是这些全连接层也可以堆叠起来，一个的输出作为另一个的输入，中间有一些隐含层。

### 6. Layers Get Stacked (各层堆叠)

[![38.png](https://i.loli.net/2018/06/04/5b154db592c44.png)](https://i.loli.net/2018/06/04/5b154db592c44.png)

最终我们把所有的层放在一起，就可以得到我们想要的结果。



