        print("Файл dz1_run.py успішно запущено")
    except subprocess.CalledProcessError as e:
        print("Помилка при виконанні dz1_run.py:", e)
    except Exception as e:
        print("Загальна помилка при запуску файлу:", e)

if __name__ == "__main__":
    main()

