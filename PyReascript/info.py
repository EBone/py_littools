#info data here

#to get mediaitem value use param below
class MediaItemInfo:
    ''''
    Get media item numerical-value attributes.
    B_MUTE : bool * to muted state
    B_LOOPSRC : bool * to loop source
    B_ALLTAKESPLAY : bool * to all takes play
    B_UISEL : bool * to ui selected
    C_BEATATTACHMODE : char * to one char of beat attached mode, -1=def, 0=time, 1=allbeats, 2=beatsosonly
    C_LOCK : char * to one char of lock flags (&1 is locked, currently)
    D_VOL : double * of item volume (volume bar)
    D_POSITION : double * of item position (seconds)
    D_LENGTH : double * of item length (seconds)
    D_SNAPOFFSET : double * of item snap offset (seconds)
    D_FADEINLEN : double * of item fade in length (manual, seconds)
    D_FADEOUTLEN : double * of item fade out length (manual, seconds)
    D_FADEINDIR : double * of item fade in curve [-1; 1]
    D_FADEOUTDIR : double * of item fade out curve [-1; 1]
    D_FADEINLEN_AUTO : double * of item autofade in length (seconds, -1 for no autofade set)
    D_FADEOUTLEN_AUTO : double * of item autofade out length (seconds, -1 for no autofade set)
    C_FADEINSHAPE : int * to fadein shape, 0=linear, ...
    C_FADEOUTSHAPE : int * to fadeout shape
    I_GROUPID : int * to group ID (0 = no group)
    I_LASTY : int * to last y position in track (readonly)
    I_LASTH : int * to last height in track (readonly)
    I_CUSTOMCOLOR : int * : custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
    I_CURTAKE : int * to active take
    IP_ITEMNUMBER : int, item number within the track (read-only, returns the item number directly)
    F_FREEMODE_Y : float * to free mode y position (0..1)
    F_FREEMODE_H : float * to free mode height (0..1)
    '''
    B_MUTE='B_MUTE'
    B_LOOPSRC='B_LOOPSRC'
    B_ALLTAKESPLAY='B_ALLTAKESPLAY'
    B_UISEL='B_UISEL'
    C_BEATATTACHMODE='C_BEATATTACHMODE'
    C_LOCK='C_LOCK'
    D_VOL='D_VOL'
    D_POSITION='D_POSITION'
    D_LENGTH='D_LENGTH'
    D_SNAPOFFSET='D_SNAPOFFSET'
    D_FADEINLEN='D_FADEINLEN'
    D_FADEOUTLEN='D_FADEOUTLEN'
    D_FADEINDIR='D_FADEINDIR'
    D_FADEOUTDIR='D_FADEOUTDIR'
    D_FADEINLEN_AUTO='D_FADEINLEN_AUTO'
    D_FADEOUTLEN_AUTO='D_FADEOUTLEN_AUTO'
    C_FADEINSHAPE='C_FADEINSHAPE'
    C_FADEOUTSHAPE='C_FADEOUTSHAPE'
    I_GROUPID='I_GROUPID'
    I_LASTY='I_LASTY'
    I_LASTH='I_LASTH'
    I_CUSTOMCOLOR='I_CUSTOMCOLOR'
    I_CURTAKE='I_CURTAKE'
    IP_ITEMNUMBER='IP_ITEMNUMBER'
    F_FREEMODE_Y='F_FREEMODE_Y'
    F_FREEMODE_H='F_FREEMODE_H'


class MediaItemTakeInfo:
    '''
    D_STARTOFFS : double *, start offset in take of item
    D_VOL : double *, take volume
    D_PAN : double *, take pan
    D_PANLAW : double *, take pan law (-1.0=default, 0.5=-6dB, 1.0=+0dB, etc)
    D_PLAYRATE : double *, take playrate (1.0=normal, 2.0=doublespeed, etc)
    D_PITCH : double *, take pitch adjust (in semitones, 0.0=normal, +12 = one octave up, etc)
    B_PPITCH, bool *, preserve pitch when changing rate
    I_CHANMODE, int *, channel mode (0=normal, 1=revstereo, 2=downmix, 3=l, 4=r)
    I_PITCHMODE, int *, pitch shifter mode, -1=proj default, otherwise high word=shifter low word = parameter
    I_CUSTOMCOLOR : int *, custom color, OS dependent color|0x100000 (i.e. ColorToNative(r,g,b)|0x100000). If you do not |0x100000, then it will not be used (though will store the color anyway).
    IP_TAKENUMBER : int, take number within the item (read-only, returns the take number directly)
    '''
    D_STARTOFFS = 'D_STARTOFFS'
    D_VOL = 'D_VOL'
    D_PAN = 'D_PAN'
    D_PANLAW = 'D_PANLAW'
    D_PLAYRATE = 'D_PLAYRATE'
    D_PITCH = 'D_PITCH'
    B_PPITCH = 'B_PPITCH'
    I_CHANMODE = 'I_CHANMODE'
    I_PITCHMODE = 'I_PITCHMODE'
    I_CUSTOMCOLOR = 'I_CUSTOMCOLOR'
    IP_TAKENUMBER = 'IP_TAKENUMBER'

