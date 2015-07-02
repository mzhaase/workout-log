# -*- coding: utf-8 -*-

"""Data Access Layer. Provides standardized interface for data access.
All getter functions return result as nested dictionary."""

def getWorkouts():
    
    
def getWorkoutByID(workoutID):
    """
    workoutID:    unique hash
    """
    
def getPreviousWorkoutResults():
    
def getPreviousWorkoutResultsByID(resultID, since = 0):
    """
    resultID:    unique hash
    since:        float, seconds since epoch
    
    Returns results for a specific workout and specific timeframe (optional).
    """
    
def setExerciseResult(exerciseID, resultID, result):
    """
    exerciseID:   unique hash
    resultID:    unique hash
    result:       dictionary
    """

    