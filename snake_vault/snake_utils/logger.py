# [+] -------------------------------------------------------------------| INFO
# [/Snake-Vault/snake_vault/snake_utils/logger.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-04 19:54:06 UTC
# updated       : 2026-06-04 19:54:06 UTC
# description   : SnakeLogger.

import inspect
from datetime import datetime
from pathlib import Path


class SnakeLogger:

    PROFILES = {
        "development": [
            "DEBUG",
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL",
        ],
        "production": [
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL",
        ],
        "quiet": [
            "ERROR",
            "CRITICAL",
        ],
    }

    def __init__(
        self,
        profile="development",
        enabled_levels=None,
        logfile=None,
        default_max_length=80,
    ):

        if enabled_levels is None:
            self.enabled_levels = self.PROFILES.get(
                profile,
                self.PROFILES["development"],
            )
        else:
            self.enabled_levels = [
                level.upper()
                for level in enabled_levels
            ]

        self.logfile = logfile
        self.default_max_length = default_max_length

    def _get_source(self):

        frame = inspect.stack()[3]
        path = Path(frame.filename)

        short_path = "/".join(
            path.parts[-3:]
        )

        return f"{short_path}:{frame.lineno}"

    def _format_message(
        self,
        message,
        verbose=False,
        max_length=None,
    ):

        message = str(message)

        if verbose:
            return message

        if max_length is None:
            max_length = self.default_max_length

        if len(message) > max_length:
            return message[:max_length] + "..."

        return message

    def _write(
        self,
        level,
        message,
        category=None,
        verbose=False,
        max_length=None,
    ):

        level = level.upper()

        if level not in self.enabled_levels:
            return

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        source = self._get_source()

        message = self._format_message(
            message,
            verbose=verbose,
            max_length=max_length,
        )

        category = category or "-"

        log_line = (
            f"{timestamp} | "
            f"{level:<8} | "
            f"{source:<35} | "
            f"{category:<15} | "
            f"{message}"
        )

        print(log_line)

        if self.logfile:
            with open(
                self.logfile,
                "a",
                encoding="utf-8",
            ) as file_handle:
                file_handle.write(log_line + "\n")

    def debug(
        self,
        message,
        category=None,
        verbose=False,
        max_length=None,
    ):

        self._write(
            "DEBUG",
            message,
            category=category,
            verbose=verbose,
            max_length=max_length,
        )

    def info(
        self,
        message,
        category=None,
        verbose=False,
        max_length=None,
    ):

        self._write(
            "INFO",
            message,
            category=category,
            verbose=verbose,
            max_length=max_length,
        )

    def warning(
        self,
        message,
        category=None,
        verbose=False,
        max_length=None,
    ):

        self._write(
            "WARNING",
            message,
            category=category,
            verbose=verbose,
            max_length=max_length,
        )

    def error(
        self,
        message,
        category=None,
        verbose=False,
        max_length=None,
    ):

        self._write(
            "ERROR",
            message,
            category=category,
            verbose=verbose,
            max_length=max_length,
        )

    def critical(
        self,
        message,
        category=None,
        verbose=False,
        max_length=None,
    ):

        self._write(
            "CRITICAL",
            message,
            category=category,
            verbose=verbose,
            max_length=max_length,
        )
