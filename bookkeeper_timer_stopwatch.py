import asyncio

class TimerTimeWatch:
    def __init__(self):
        self.stopwatch_running = False
        self.timer_running = False
        self.SW_seconds = 0

    async def stopwatch(self, callback):
        """Асинхронний секундомір (від 0 до ∞)"""
        self.stopwatch_running = True
        # SW_seconds = 0
        while self.stopwatch_running:
            callback(self.SW_seconds)  # Викликає функцію для оновлення інтерфейсу
            await asyncio.sleep(1)
            self.SW_seconds += 1
    
    def stop_stopwatch(self):
        """Зупинка секундоміра"""
        self.stopwatch_running = False
        self.SW_seconds = 0
    
    def pause_stopwatch(self):
        """Пауза секундоміра"""
        self.stopwatch_running = False
        
    
    
    async def timer(self, seconds, callback):
        """Асинхронний таймер (від заданого числа до 0)"""
        self.timer_running = True
        while seconds >= 0 and self.timer_running:
            callback(seconds)  # Викликає функцію для оновлення інтерфейсу
            await asyncio.sleep(1)
            seconds -= 1

    def stop_timer(self):
        """Зупинка таймера"""
        self.timer_running = False
