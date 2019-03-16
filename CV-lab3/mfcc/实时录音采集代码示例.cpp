
// 创新研修课代码Dlg.cpp : 实现文件
//

#include "stdafx.h"


#include "Mmsystem.h"
#pragma  comment(lib,"Winmm.lib")



static void CALLBACK waveInProc(HWAVEIN hwi, UINT uMsg, WORD dwInstance,
	WAVEHDR* dwParam1, DWORD dwParam2);
void startwork( );//开始录音采集
void closewave();



#define MAXWAVEBLOCK  100//输入内存块数
#define MAXWAVEBUFFER 400//每块内存大小


bool m_Opened;          //当前录音状态，false-停止录音  true-正在录音
static WAVEHDR WaveHdrIn[MAXWAVEBLOCK];  //录音数据文件头
static char WaveInBuffer[MAXWAVEBLOCK][MAXWAVEBUFFER];//记录录音数据用内存块
static HWAVEIN hWaveIn;
int flag=0;


void startwork( )
{



	int i;

	//初始化录音设备
	WAVEFORMATEX waveFormatEx;
	waveFormatEx.cbSize=0;
	waveFormatEx.nAvgBytesPerSec=16000;
	waveFormatEx.nBlockAlign=2;
	waveFormatEx.nChannels=1;
	waveFormatEx.nSamplesPerSec=8000;
	waveFormatEx.wBitsPerSample=16;
	waveFormatEx.wFormatTag=WAVE_FORMAT_PCM;
	hWaveIn = NULL;
	if(waveInOpen(&hWaveIn, WAVE_MAPPER, &waveFormatEx, (unsigned long)waveInProc, 1L, CALLBACK_FUNCTION)) 
	{
		::MessageBoxW(0,_T("声卡设置失败"),_T("信息窗口"),0);
		return;//录音设备打开失败，可能声卡不支持全双工。
	}


	for(i=0;i < MAXWAVEBLOCK; i++)
	{//增加录音内存
		WaveHdrIn[i].lpData=WaveInBuffer[i];
		WaveHdrIn[i].dwBufferLength=MAXWAVEBUFFER;
		WaveHdrIn[i].dwFlags=0;
		WaveHdrIn[i].dwUser=0;
		if(waveInPrepareHeader(hWaveIn, &WaveHdrIn[i], sizeof(WAVEHDR)))
		{//无法锁定该内存
			closewave();
			::MessageBoxW(0,_T("声卡设置失败"),_T("信息窗口"),0);
			return;
		}; 
		if(waveInAddBuffer(hWaveIn,&WaveHdrIn[i],sizeof(WAVEHDR)))
		{//无法增加该内存
			closewave();
			::MessageBoxW(0,_T("声卡设置失败"),_T("信息窗口"),0);
			return;
		}
	}
	
	
	//打开声卡
	waveInStart(hWaveIn);



}
void closewave()
{
   
	 if(hWaveIn){
		waveInStop(hWaveIn);//停止录音
		waveInReset(hWaveIn);//清空录音缓存
		waveInClose(hWaveIn);//关闭录音设备
		hWaveIn = NULL;

	}
	
}



static void CALLBACK waveInProc(HWAVEIN hwi, UINT uMsg, WORD dwInstance,
	WAVEHDR* dwParam1, DWORD dwParam2)
{

	char buffer[MAXWAVEBUFFER];
	long buf_len;
	int i;

	switch(uMsg)
	{//判断回调类型
	case WIM_OPEN:
		//录音设备正常打开时，触发该事件
		//MessageBox(NULL,"Open success", "提示", MB_OK);
		break;
	case WIM_CLOSE:
		//录音设备正常关闭时，触发该事件
		//MessageBox(NULL,"Close success", "提示", MB_OK);
		break;
	case WIM_DATA:
		//录音设备返回数据时，触发该事件
		if(flag==0) break;
		if(!waveInUnprepareHeader(hwi, dwParam1,sizeof(WAVEHDR)))
		{//可以释放内存。有的情况虽然返回数据，但不能释放内存，
			//如使用同一个WAVEHDR增加多个内存块时，会出现上述情况

			buf_len = dwParam1->dwBytesRecorded;//记录录音数据长度
			memcpy(buffer, dwParam1->lpData , buf_len);//复制返回数据
			// to do your code
			
			dwParam1->dwUser=0;//恢复设置
			dwParam1->dwBufferLength=MAXWAVEBUFFER;
			dwParam1->dwFlags=0;
			
			waveInPrepareHeader(hwi,dwParam1,sizeof(WAVEHDR));
			waveInAddBuffer(hwi,dwParam1,sizeof(WAVEHDR));
		}//if unprepare suceessed

		break;
	}
}

