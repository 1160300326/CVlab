#if !defined(KWS_MFCC__INCLUDED_)
#define KWS_MFCC__INCLUDED_
#define     FS 16.0F       
#define     PI 3.1415926536F   
#define     FiltNum 25
#define     FFTLen  512
#define     H_FRAME 200
#define     FRAMEL  400
#define     Frame  400
#define     FRAMELL 401
#define     PCEP    12 

class MFCC{
private:
   float   FiltCoe1[FFTLen/2+1];
   float   FiltCoe2[FFTLen/2+1];
   _int16  Num[FFTLen/2+1];
   void InitFilt();
   _int16 CFilt(float *,float *En);
   void fft(float *,float *,_int16);
   void MultiHamming(float *data);
   void GetVector(float *, float *);
public:
	MFCC();
    virtual ~MFCC();
    void GetFeature(short *, float *,int);//参数1--数据包指针 参数2-特征矢量指针  参数3-数据字节长度
};
#endif