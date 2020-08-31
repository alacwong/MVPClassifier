from scripts.numpy_util import binarize


def validate_accuracy(model, sample, soln) -> float:
    pred = model.predict(sample)
    total = 0
    correct = 0
    for i in range(len(pred)):
        if binarize(pred[i]) == soln[i]:
            correct += 1
        total += 1
    return correct/total