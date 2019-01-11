## 创建与初始化
```c
int rows = 3, cols = 1;
cv::Size size(cols, rows);

/* first method */
cv::Mat myMat( rows, cols, CV_8UC1, cv::Scalar(0) );
cv::Mat myMat = cv::Mat( rows, cols, CV_8UC1, cv::Scalar(0) );

cv::Mat myMat( size, CV_8UC1, cv::Scalar(0) );
cv::Mat myMat( cv::Size(cols, rows), CV_8UC1, cv::Scalar(0) );

/* second method */
cv::Mat myMat2;
myMat = cv::Mat( rows, cols, CV_8UC1 );
// initial with other mat or data
myMat.copyTo(myMat2);         // initial with mat

cv::Point3i pts( 1, 2, 3 );   
myMat2 = cv::Mat(pts, true);  // initial with other data

cv::Mat_<double> myMat_ = ( cv::Mat_<double>(3, 3) <<
    1.0, 2.0, 3.0,
    4.0, 5.0, 6.0,
    7.0, 8.0, 9.0);

cv::Mat_<double> myMat_ = cv::Mat_<double>::zeros(3, 3); // others: eyes, diag, ones
```
***注意：***
```
使用Mat::Mat(int rows, int cols, int type, const Scalar& s)
和Mat::Mat(Size size, int type, const Scalar& s)函数进行Mat初始化的时候，一定要注意Size行列存放顺序是
(col, row)或者是(width, height)；
Mat的type种类非常多，可以创建普通的CV_8UC1, ... , CV_64FC41-4通道的矩阵,
也可以创建更高通道的矩阵CV_8UC(n), ... , CV_64FC(n),
其中最大可以达到CV_CN_MAX通道，Opencv 2.4.11版本中#define CV_CN_MAX 512;
创建多通道Mat时，例如CV_8UC3，使用cv::Scalar(0, 0,0)或myMat.setTo(cv::Scalar(0)),
其中后者通用于任意通道；
使用其他Mat拷贝初始化的时候，void Mat::copyTo(OutputArray m)
const函数会首先调用m.create(this->size(), this->type())
所以会对输入的m进行重新创建（包括size和type），然后进行数据拷贝。m.copyTo(m)也是允许的，没有任何问题。
```
## 数据访问
```c
//Pointer
cv::Mat image = cv::imread( "E:\\test.JPG", CV_LOAD_IMAGE_GRAYSCALE );
const int rows = image.rows;
const int cols = image.cols;

uchar* data = (uchar*)image.data;
for ( int i=0; i<rows; i++ )
{
    for ( int j=0; j<cols; j++ )
    {
        int index = i*cols + j;
        data[index] = 0;
        /*
            if color one:
            data[index * 3 + 0] = 0；
            data[index * 3 + 1] = 0;
            data[index * 3 + 2] = 0;
        */
    }
}
/*
    // also can be used as follow:
    for ( int i=0; i<rows; i++ )
    {
        uchar* data = (uchar*)image.data + i*cols;
        for ( int j=0; j<cols; j++ )
        {
            *data++ = 0;
        }
    }
}
*/
// cv::imwrite( "E:\\test2.JPG", image );
```
```c
/* .ptr with [] */
for ( int i=0; i<rows; i++ )
{
    uchar *data = image.ptr<uchar>( i );
    for ( int j=0; j<cols; j++ )
    {
        data[j] = 0;
        /*
            if color one:
            data[j*3 + 0] = 0;
            data[j*3 + 1] = 0;
            data[j*3 + 2] = 0;
        */
    }
}

/* .ptr with pointer */
for ( int i=0; i<rows; i++ )
{
    uchar *data = image.ptr<uchar>( i );
    for ( int j=0; j<cols*image; j++ )
    {
        *data++ = 0;
    }
}
```
```c
for ( int i=0; i<rows; i++ )
{
    for ( int j=0; j<cols; j++ )
    {
         image.at<uchar>(i, j)= 0;
         // also can be: image.at<uchar>( cv::Point(j, i) ) = 0;
         /*
             if color one:
             image.at<uchar>( i, j*3 + 0 ) = 0;
             image.at<uchar>( i, j*3 + 1 ) = 0;
             image.at<uchar>( i, j*3 + 2 ) = 0;
         */
    }
}
```
