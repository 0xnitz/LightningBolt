#ifndef _IPOGAN_H_
#define _IPOGAN_H_

class IPogan
{
public:
	virtual void CleanUp() = 0;
	virtual void Deploy() = 0;
	virtual void SendToHome() = 0;
};

#endif
