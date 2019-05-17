# 处理文件
## 连接FCS文件，标准化FCS文件
```R


# 1. 设置工作路径并获取
setwd("E:/Biology/data/Live_cells_clustered")
setwd("E:/Biology/workspace/")
fcs.path <- getwd()
# 2. 读取需要的合并的文件列表
files <-dir('.')
# 或者 list.files('./data/Live_cells_clustered/')
# 拼接文件绝对路径
file.location <- paste(fcs.path, files, sep='/')

# 3. 读取一系列FCS文件为flowFrame
library(flowCore)
# 或者
# raw_data <- read.flowSet(files, fcs.path)
# 读取所有的M样本
frm <- read.flowSet(path='./M/')
# 合并文件
library(CATALYST)
ff <- concatFCS(frm)

# 4. 标准化文件
# 获取所有文件名
all.files<-list.files(all.files=TRUE, full.names=TRUE, recursive=TRUE, include.dirs=FALSE)
normCytof(x=ft, out_path="../",y="dvs", k=80, plot=FALSE)
```

## debarcoding 工作流

debarcoding方案应该是一个二进制表，其中样本ID为行，数字条形码为列名
### 1. assignPrelim: Assignment of preliminary IDs（初步ID分配）
assignPrelim 返回一个dbFrame对象
包含：
	- exprs 来自输入的floFrame
	- slot中 bc_ids的时间分配的数字或字符向量，
	- deltas 在插槽增量中标准化尺度上的条形码群体之间的分离
	- normed_bcs slot中标准化条形码强度
	- counts yields 矩阵
```R
data(sample_ff)  # sample_ff 为flowFrame
data(sample_key) # debarcoding scheme 一个二进制表格，行为样本id,数值barcode mass为列名

re0 <- assignPrelim(x=sample_ff, y=sample_key, verbose=FALSE)
# estimate separation cutoffs
re <- estCutoffs(x=re0)
# use global separation cutoff
applyCutoffs(x=re, sep_cutoffs=0.35)

# use population-specific cutoffs
re <- applyCutoffs(x=re)
outFCS(x=re, y=sample_ff)

plotYields(x=re, which=c("C1", 0), plotly=FALSE)

# event plots for unassigned events
# & barcode population D1
plotEvents(x=re, which=c(0, "D1"), n_events=25)

plotMahal(x=re, which="B3")

```
### 2. estCutoffs: Estimation of separation cutoffs
与单一的全局截取相反，estCutoffs将估计特定样本的截止值，以处理通过异步方式下降产生的条形码群体细胞
选择条形码阈值的方式：1）自动，2）根据各自的条形码
检查产量图（见下文），检查并可能改进分离截止值
标记平缓结束点和开始急剧下降的点

### 3. applyCutoffs: Applying deconvolution parameters
### 4. outFCS: Output population-wise FCS files
### 5. plotYields: Selecting barcode separation cutoffs
### 6. plotEvents: Normalized intensities
### 7. plotMahal: All barcode biaxial plot

## compensation

