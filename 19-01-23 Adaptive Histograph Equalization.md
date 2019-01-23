# Adaptive Histogram Equalization
```c

	cv::Mat bgr_image = cv::imread("img.png");
	cv::Mat lab_image;
	cv::cvtColor(bgr_image, lab_image, CV_BGR2Lab);

	// Estrazione L channel
	std::vector<cv::Mat> lab_planes(3);
	cv::split(lab_image, lab_planes);

	// CLAHE algorithm per L channel
	cv::Ptr<cv::CLAHE> clahe = cv::createCLAHE();
	clahe->setClipLimit(2);
	cv::Mat dst;
	clahe->apply(lab_planes[0], dst);

	// Merge
	dst.copyTo(lab_planes[0]);
	cv::merge(lab_planes, lab_image);

	// RGB
	cv::Mat image_clahe;
	cv::cvtColor(lab_image, image_clahe, CV_Lab2BGR);

	// out
	cv::imshow("image original", bgr_image);
	cv::imshow("image CLAHE", image_clahe);
	cv::waitKey(0);
```
