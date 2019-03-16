
// �������޿δ���Dlg.cpp : ʵ���ļ�
//

#include "stdafx.h"


#include "Mmsystem.h"
#pragma  comment(lib,"Winmm.lib")



static void CALLBACK waveInProc(HWAVEIN hwi, UINT uMsg, WORD dwInstance,
	WAVEHDR* dwParam1, DWORD dwParam2);
void startwork( );//��ʼ¼���ɼ�
void closewave();



#define MAXWAVEBLOCK  100//�����ڴ����
#define MAXWAVEBUFFER 400//ÿ���ڴ��С


bool m_Opened;          //��ǰ¼��״̬��false-ֹͣ¼��  true-����¼��
static WAVEHDR WaveHdrIn[MAXWAVEBLOCK];  //¼�������ļ�ͷ
static char WaveInBuffer[MAXWAVEBLOCK][MAXWAVEBUFFER];//��¼¼���������ڴ��
static HWAVEIN hWaveIn;
int flag=0;


void startwork( )
{



	int i;

	//��ʼ��¼���豸
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
		::MessageBoxW(0,_T("��������ʧ��"),_T("��Ϣ����"),0);
		return;//¼���豸��ʧ�ܣ�����������֧��ȫ˫����
	}


	for(i=0;i < MAXWAVEBLOCK; i++)
	{//����¼���ڴ�
		WaveHdrIn[i].lpData=WaveInBuffer[i];
		WaveHdrIn[i].dwBufferLength=MAXWAVEBUFFER;
		WaveHdrIn[i].dwFlags=0;
		WaveHdrIn[i].dwUser=0;
		if(waveInPrepareHeader(hWaveIn, &WaveHdrIn[i], sizeof(WAVEHDR)))
		{//�޷��������ڴ�
			closewave();
			::MessageBoxW(0,_T("��������ʧ��"),_T("��Ϣ����"),0);
			return;
		}; 
		if(waveInAddBuffer(hWaveIn,&WaveHdrIn[i],sizeof(WAVEHDR)))
		{//�޷����Ӹ��ڴ�
			closewave();
			::MessageBoxW(0,_T("��������ʧ��"),_T("��Ϣ����"),0);
			return;
		}
	}
	
	
	//������
	waveInStart(hWaveIn);



}
void closewave()
{
   
	 if(hWaveIn){
		waveInStop(hWaveIn);//ֹͣ¼��
		waveInReset(hWaveIn);//���¼������
		waveInClose(hWaveIn);//�ر�¼���豸
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
	{//�жϻص�����
	case WIM_OPEN:
		//¼���豸������ʱ���������¼�
		//MessageBox(NULL,"Open success", "��ʾ", MB_OK);
		break;
	case WIM_CLOSE:
		//¼���豸�����ر�ʱ���������¼�
		//MessageBox(NULL,"Close success", "��ʾ", MB_OK);
		break;
	case WIM_DATA:
		//¼���豸��������ʱ���������¼�
		if(flag==0) break;
		if(!waveInUnprepareHeader(hwi, dwParam1,sizeof(WAVEHDR)))
		{//�����ͷ��ڴ档�е������Ȼ�������ݣ��������ͷ��ڴ棬
			//��ʹ��ͬһ��WAVEHDR���Ӷ���ڴ��ʱ��������������

			buf_len = dwParam1->dwBytesRecorded;//��¼¼�����ݳ���
			memcpy(buffer, dwParam1->lpData , buf_len);//���Ʒ�������
			// to do your code
			
			dwParam1->dwUser=0;//�ָ�����
			dwParam1->dwBufferLength=MAXWAVEBUFFER;
			dwParam1->dwFlags=0;
			
			waveInPrepareHeader(hwi,dwParam1,sizeof(WAVEHDR));
			waveInAddBuffer(hwi,dwParam1,sizeof(WAVEHDR));
		}//if unprepare suceessed

		break;
	}
}

