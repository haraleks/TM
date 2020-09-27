from datetime import datetime


def get_file_type(filename: str):
    img_suffixs = ['img', 'svg', 'png', 'jpeg', 'jpg']
    video_suffixs = ['avi', 'mkv', 'mov', 'dvd', 'mpeg', 'gif']
    audio_suffixs = ['ac3', 'amr', 'mp3']
    file_suffix = filename[filename.rindex('.') + 1:]
    if file_suffix in img_suffixs:
        return 'img', file_suffix
    elif file_suffix in video_suffixs:
        return 'video', file_suffix
    elif file_suffix in audio_suffixs:
        return 'audio', file_suffix
    else:
        return 'unknown', file_suffix


def path_to_upload_file(instance, filename, *args, **kwargs):
    file_type, file_suffix = get_file_type(filename)
    filename = '.'.join(
        [datetime.strftime(datetime.now(), '%Y/%m/%d_%H%M%S'), file_suffix]
    )
    return '/'.join([file_type, filename])